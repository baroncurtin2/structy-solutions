def overlap_subsequence(string1: str, string2: str) -> int:
    return _overlap_sequence(string1, string2, 0, 0, {})


def _overlap_sequence(s1: str, s2: str, ind1: int, ind2: int, memo: dict) -> int:
    key = (ind1, ind2)

    if key in memo:
        return memo[key]

    if ind1 == len(s1) or ind2 == len(s2):
        return 0

    if s1[ind1] == s2[ind2]:
        memo[key] = 1 + _overlap_sequence(s1, s2, ind1 + 1, ind2 + 1, memo)
    else:
        memo[key] = max(
            _overlap_sequence(s1, s2, ind1 + 1, ind2, memo), _overlap_sequence(s1, s2, ind1, ind2 + 1, memo)
        )

    return memo[key]
