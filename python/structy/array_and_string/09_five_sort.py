def five_sort(nums: list[int]) -> list[int]:
    # Two pointer solution
    # Time: O(n)
    # Space: O(1)
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[j] == 5:
            j -= 1
        elif nums[i] == 5:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        else:
            i += 1
    return nums
