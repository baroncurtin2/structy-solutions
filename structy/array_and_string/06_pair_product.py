def pair_product(numbers: list[int], target_product: int) -> (int, int):
    # Time: O(n)
    # Space: O(n)    
    previous = {}

    for i, n in enumerate(numbers):
        complement = target_product / n

        if complement in previous.keys():
            return i, previous[complement]
        previous[n] = i