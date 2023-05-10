from collections import deque


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_sorted = merge_sort(nums[:mid])
    right_sorted = merge_sort(nums[mid:])
    return merge(left_sorted, right_sorted)


def merge(left: list[int], right: list[int]) -> list[int]:
    merged = []

    left, right = deque(left), deque(right)

    while left and right:
        if left[0] < right[0]:
            merged.append(left.popleft())
        else:
            merged.append(right.popleft())

    merged += left
    merged += right

    return merged
