

from __future__ import annotations

import json
import random
import re
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import config
from src.utils.logger import get_logger
from src.utils.rate_limiter import RateLimiterConfig, TokenBucketRateLimiter

logger = get_logger(__name__)

SEARCH_URL_TEMPLATE = "https://x.com/search?q={query}&src=typed_query&f=live"

DESKTOP_USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
]


@dataclass
class RawTweet:
    tweet_id: str
    username: str
    display_name: str
    timestamp: str  # ISO 8601, from the <time datetime="..."> attribute
    content: str
    likes: int
    retweets: int
    replies: int
    hashtag_source: str  # which search query surfaced this tweet
    scraped_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class TwitterScraper:
    def __init__(
        self,
        cookies_path: str | Path = "cookies.json",
        headless: bool = config.HEADLESS,
    ):
        self.cookies_path = Path(cookies_path)
        self.headless = headless
        self.driver: webdriver.Chrome | None = None
        self.rate_limiter = TokenBucketRateLimiter(
            RateLimiterConfig(
                max_calls=config.RATE_LIMIT_MAX_CALLS,
                period_seconds=config.RATE_LIMIT_PERIOD_SECONDS,
            )
        )
        self._seen_ids: set[str] = set()

    def _build_driver(self) -> webdriver.Chrome:
        opts = Options()
        if self.headless:
            opts.add_argument("--headless=new")
        opts.add_argument("--window-size=1400,1000")
        opts.add_argument("--disable-blink-features=AutomationControlled")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--no-sandbox")
        opts.add_argument(f"user-agent={random.choice(DESKTOP_USER_AGENTS)}")
        # Remove the two most common automation fingerprints.
        opts.add_experimental_option("excludeSwitches", ["enable-automation"])
        opts.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(options=opts)
        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"},
        )
        return driver

    

    def _load_cookies(self) -> None:
        if not self.cookies_path.exists():
            logger.warning(
                "No cookies file found at %s. X's search page generally "
                "requires an authenticated session; export cookies from a "
                "logged-in browser (see README) before running a live "
                "collection run.",
                self.cookies_path,
            )
            return
        assert self.driver is not None
        self.driver.get("https://x.com")
        cookies = json.loads(self.cookies_path.read_text(encoding="utf-8"))
        for cookie in cookies:
            cookie.pop("sameSite", None)
            try:
                self.driver.add_cookie(cookie)
            except Exception as exc:  # noqa: BLE001 - cookie quirks vary by export tool
                logger.debug("Skipped cookie %s: %s", cookie.get("name"), exc)
        self.driver.refresh()

    def __enter__(self) -> "TwitterScraper":
        self.driver = self._build_driver()
        self._load_cookies()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        if self.driver is not None:
            self.driver.quit()


    @staticmethod
    def _parse_metric(text: str) -> int:
        """Converts X's compact metric strings ('1.2K', '3,401', '') to int."""
        if not text:
            return 0
        text = text.strip().replace(",", "")
        multiplier = 1
        if text.endswith("K"):
            multiplier, text = 1_000, text[:-1]
        elif text.endswith("M"):
            multiplier, text = 1_000_000, text[:-1]
        try:
            return int(float(text) * multiplier)
        except ValueError:
            return 0

    def _extract_tweet(self, article, hashtag_source: str) -> RawTweet | None:
        try:
            link_el = article.find_element(By.CSS_SELECTOR, 'a[href*="/status/"]')
            href = link_el.get_attribute("href") or ""
            match = re.search(r"/status/(\d+)", href)
            if not match:
                return None
            tweet_id = match.group(1)

            username_el = article.find_element(By.CSS_SELECTOR, 'div[data-testid="User-Name"]')
            username_text = username_el.text
            # username_text typically looks like "Display Name\n@handle\n..."
            handle_match = re.search(r"@(\w+)", username_text)
            username = handle_match.group(1) if handle_match else "unknown"
            display_name = username_text.split("\n")[0] if username_text else "unknown"

            time_el = article.find_element(By.TAG_NAME, "time")
            timestamp = time_el.get_attribute("datetime") or ""

            try:
                content = article.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetText"]').text
            except NoSuchElementException:
                content = ""

            def metric(testid: str) -> int:
                try:
                    el = article.find_element(By.CSS_SELECTOR, f'div[data-testid="{testid}"]')
                    return self._parse_metric(el.text)
                except NoSuchElementException:
                    return 0

            replies = metric("reply")
            retweets = metric("retweet")
            likes = metric("like")

            return RawTweet(
                tweet_id=tweet_id,
                username=username,
                display_name=display_name,
                timestamp=timestamp,
                content=content,
                likes=likes,
                retweets=retweets,
                replies=replies,
                hashtag_source=hashtag_source,
            )
        except (NoSuchElementException, StaleElementReferenceException):
            return None

    # ------------------------------------------------------------------ #
    # Collection loop
    # ------------------------------------------------------------------ #
    def collect_for_hashtag(self, hashtag: str, max_tweets: int) -> Iterator[RawTweet]:
        assert self.driver is not None
        url = SEARCH_URL_TEMPLATE.format(query=hashtag.replace("#", "%23"))
        self.rate_limiter.acquire()
        self.driver.get(url)

        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'article[data-testid="tweet"]'))
            )
        except TimeoutException:
            logger.error(
                "Timed out waiting for results on %s -- likely blocked by a "
                "login wall or interstitial. See README for cookie setup.",
                hashtag,
            )
            return

        collected = 0
        stale_scrolls = 0
        scrolls = 0

        while (
            collected < max_tweets
            and scrolls < config.MAX_SCROLLS_PER_HASHTAG
            and stale_scrolls < config.STALE_SCROLL_LIMIT
        ):
            articles = self.driver.find_elements(By.CSS_SELECTOR, 'article[data-testid="tweet"]')
            new_this_pass = 0

            for article in articles:
                tweet = self._extract_tweet(article, hashtag)
                if tweet is None or tweet.tweet_id in self._seen_ids:
                    continue
                self._seen_ids.add(tweet.tweet_id)
                new_this_pass += 1
                collected += 1
                yield tweet
                if collected >= max_tweets:
                    break

            stale_scrolls = stale_scrolls + 1 if new_this_pass == 0 else 0

            scroll_distance = random.randint(800, 1800)
            self.driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
            self.rate_limiter.acquire()
            time.sleep(random.uniform(*config.SCROLL_PAUSE_RANGE))
            scrolls += 1

        logger.info(
            "Finished '%s': collected=%d, scrolls=%d, stale_scrolls_at_stop=%d",
            hashtag, collected, scrolls, stale_scrolls,
        )

    def collect_all(self, hashtags: list[str] | None = None, target_total: int = config.MIN_TWEETS_TARGET) -> list[RawTweet]:
        hashtags = hashtags or config.TARGET_HASHTAGS
        per_tag_target = max(1, target_total // len(hashtags))
        results: list[RawTweet] = []

        for tag in hashtags:
            remaining = target_total - len(results)
            if remaining <= 0:
                break
            tag_target = max(per_tag_target, remaining if tag == hashtags[-1] else per_tag_target)
            logger.info("Collecting up to %d tweets for %s", tag_target, tag)
            for tweet in self.collect_for_hashtag(tag, tag_target):
                results.append(tweet)

        logger.info("Collection complete: %d unique tweets across %d hashtags", len(results), len(hashtags))
        return results


def run_collection(output_path: str | Path, target_total: int = config.MIN_TWEETS_TARGET) -> Path:
    """Entry point used by main.py / CLI."""
    from src.storage import ParquetStorage  # local import avoids circulars

    with TwitterScraper() as scraper:
        tweets = scraper.collect_all(target_total=target_total)

    storage = ParquetStorage(output_path)
    storage.write_raw([t.__dict__ for t in tweets])
    return Path(output_path)
