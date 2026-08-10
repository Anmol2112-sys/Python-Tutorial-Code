
def count_even_odd(arr):
    even = 0
    odd = 0

    for i in arr:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


nums = [20, 25, 14, 19, 16, 24, 28, 47, 26]

even, odd = count_even_odd(nums)

print("Even Numbers:", even)
print("Odd Numbers:", odd)

