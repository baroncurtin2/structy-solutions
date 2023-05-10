def quickest_concat(s: str, words: list[str]) -> int:
    result = _quickest_concat(s, words, {})

    return -1 if result == float("inf") else result


def _quickest_concat(s: str, words: list[str], memo: dict) -> int:
    if s in memo:
        return memo[s]

    if not s:
        return 0

    min_words = float("inf")

    for word in words:
        if s.startswith(word):
            n = len(word)
            suffix = s[n:]

            attempt = 1 + _quickest_concat(suffix, words, memo)
            min_words = min(attempt, min_words)

    memo[s] = min_words
    return min_words
