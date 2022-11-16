def max_value(nums: list[int]) -> int:
    max_val = float("-inf")

    for n in nums:
        if n > max_val:
            max_val = n

    return max_val
