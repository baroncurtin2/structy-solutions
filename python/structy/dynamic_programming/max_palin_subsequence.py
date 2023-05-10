def max_palin_subsequence(string: str) -> int:
    return _max_palin_subsequence(string, 0, len(string) - 1, {})


def _max_palin_subsequence(string: str, start: int, end: int, memo: dict) -> int:
    key = (start, end)

    if key in memo:
        return memo[key]

    if start == end:
        return 1

    if start > end:
        return 0

    if string[start] == string[end]:
        memo[key] = 2 + _max_palin_subsequence(string, start + 1, end - 1, memo)
    else:
        memo[key] = max(
            _max_palin_subsequence(string, start + 1, end, memo),
            _max_palin_subsequence(string, start, end - 1, memo),
        )

    return memo[key]
