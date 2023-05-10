def intersection(a: list[int], b: list[int]) -> list[int]:
    # Time: O(n+m)
    # Space: O(n)
    set_a = set(a)
    return [item for item in b if item in set_a]
