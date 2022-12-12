def tribonacci(n: int) -> int:
    memo = [-1] * (n + 1)

    return _tribonacci(n, memo)


def _tribonacci(n: int, memo: list[int]) -> int:
    if n <= 1:
        return 0

    if n == 2:
        return 1

    if memo[n] >= 0:
        return memo[n]

    memo[n] = sum(_tribonacci(n + x, memo) for x in range(-3, 0))
    return memo[n]
