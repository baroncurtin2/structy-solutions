def binary_search(numbers: list[int], target: int) -> int:
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (high + low) // 2
        mid_value = numbers[mid]

        if target == mid_value:
            return mid

        if target > mid_value:
            low = mid + 1
        else:
            high = mid - 1

    return -1
