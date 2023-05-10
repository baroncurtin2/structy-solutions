def pair_sum(numbers: list[int], target_sum: int) -> (int, int):
    # Time: O(n)
    # Space: O(n)
    previous = {}

    for i, n in enumerate(numbers):
        complement = target_sum - n

        if complement in previous.keys():
            return previous[complement], i

        previous[n] = i
