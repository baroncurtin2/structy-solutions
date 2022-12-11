def fib(n: int) -> int:
    memo = [-1] * (n + 1)

    return _fib(n, memo)


def _fib(n: int, memo: list[int]) -> int:
    if n <= 1:
        return n

    if memo[n] >= 0:
        return memo[n]

    memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
    return memo[n]
