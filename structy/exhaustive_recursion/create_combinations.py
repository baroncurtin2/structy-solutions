def create_combinations(items: list[str | int], k: int) -> list[list[str | int]]:
    # n = length of items
    # k = target length
    # Time: ~O(n choose k)
    # Space: ~O(n choose k)
    if k > len(items):
        return []

    if k == 0:
        return [[]]

    first = items[0]
    remaining = items[1:]

    combos_with_first = [[first, *partial_combo] for partial_combo in create_combinations(remaining, k - 1)]
    combos_without_first = create_combinations(remaining, k)
    return combos_with_first + combos_without_first
