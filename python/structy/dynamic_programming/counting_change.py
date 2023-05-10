def counting_change(amount: int, coins: list[int]) -> int:
    return _counting_change(amount, coins, 0, {})


def _counting_change(amount: int, coins: list[int], i: int, memo: dict) -> int:
    key = (amount, i)

    if key in memo:
        return memo[key]

    if amount == 0:
        return 1

    if i == len(coins):
        return 0

    total = 0
    coin = coins[i]

    for qty in range(amount // coin + 1):
        remainder = amount - (qty * coin)
        total += _counting_change(remainder, coins, i + 1, memo)

    memo[key] = total
    return total
