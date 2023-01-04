def create_combinations(items: list[str]) -> list[list[str]]:
    if not items:
        return [[]]

    first = items[0]
    remaining = items[1:]

    return [perm[:i] + [first] + perm[i:] for perm in create_combinations(remaining) for i in range(len(perm) + 1)]


def permutations_with_tail_call_optimization(items: list[str]) -> list[list[str]]:
    def helper(items: list[str], prefix: list[str]) -> list[list[str]]:
        if not items:
            return [prefix]

        result = []

        for i, item in enumerate(items):
            result.extend(helper(items[:i] + items[i + 1 :], prefix + [item]))
        return result

    return helper(items, [])
