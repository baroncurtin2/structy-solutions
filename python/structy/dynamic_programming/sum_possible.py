def sum_possible(amount: int, numbers: list[int]) -> bool:
    return _sum_possible(amount, numbers, {})


def _sum_possible(amount: int, numbers: list[int], memo: dict) -> bool:
    if amount in memo:
        return memo[amount]

    if amount < 0:
        return False

    if amount == 0:
        return True

    for num in numbers:
        if _sum_possible(amount - num, numbers, memo):
            memo[amount] = True
            return True

    memo[amount] = False
    return False
