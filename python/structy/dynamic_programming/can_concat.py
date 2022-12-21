def can_concat(s: str, words: list[str]) -> bool:
    # s = length of string
    # w = # of words
    # Time: ~O(sw)
    # Space: O(s)
    return _can_concat(s, words, {})


def _can_concat(s: str, words: list[str], memo: dict) -> bool:
    if s in memo:
        return memo[s]

    if not s:
        return True

    for word in words:
        if s.startswith(word):
            n = len(word)
            suffix = s[n:]

            if _can_concat(suffix, words, memo):
                memo[s] = True
                return True

    memo[s] = False
    return False
