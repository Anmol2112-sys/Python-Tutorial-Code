

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

import config
from src.utils.logger import get_logger

logger = get_logger(__name__)


class ParquetStorage:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def write_raw(self, records: list[dict]) -> None:
        df = pd.DataFrame.from_records(records)
        table = pa.Table.from_pandas(df, preserve_index=False)
        pq.write_table(table, self.path, compression=config.PARQUET_COMPRESSION)
        logger.info("Wrote %d raw records to %s", len(df), self.path)

    def write_processed(self, df: pd.DataFrame) -> None:
        table = pa.Table.from_pandas(df, preserve_index=False)
        pq.write_table(table, self.path, compression=config.PARQUET_COMPRESSION)
        logger.info("Wrote %d processed records to %s", len(df), self.path)

    def write_partitioned_by_date(self, df: pd.DataFrame, base_dir: str | Path, date_col: str = "timestamp") -> None:
        """Writes one parquet file per UTC date -- keeps individual files small
        and lets analysis code read only the date range it needs."""
        base_dir = Path(base_dir)
        base_dir.mkdir(parents=True, exist_ok=True)
        df = df.copy()
        df["_date"] = pd.to_datetime(df[date_col], utc=True).dt.date

        for date_val, group in df.groupby("_date"):
            out_path = base_dir / f"tweets_{date_val}.parquet"
            table = pa.Table.from_pandas(group.drop(columns=["_date"]), preserve_index=False)
            pq.write_table(table, out_path, compression=config.PARQUET_COMPRESSION)
            logger.info("Partition %s: %d rows -> %s", date_val, len(group), out_path)

    def read(self, columns: list[str] | None = None) -> pd.DataFrame:
        return pq.read_table(self.path, columns=columns).to_pandas()

    @staticmethod
    def read_partitioned(base_dir: str | Path, columns: list[str] | None = None) -> pd.DataFrame:
        base_dir = Path(base_dir)
        files = sorted(base_dir.glob("*.parquet"))
        if not files:
            return pd.DataFrame()
        frames = [pq.read_table(f, columns=columns).to_pandas() for f in files]
        return pd.concat(frames, ignore_index=True)
