from collections import defaultdict

Number = float | int


def max_increasing_subseq(numbers: list[int], recur: bool = False) -> int:
    # n = length of the list
    # Time: O(n^2)
    # Space: O(n^2)
    if recur:
        return _max_increasing_subseq(numbers, 0, float("-inf"), {})
    return max_increasing_subseq_iter(numbers)


def _max_increasing_subseq(numbers: list[int], i: int, previous: Number, memo: dict) -> int:
    key = (i, previous)

    if key in memo:
        return memo[key]

    if i == len(numbers):
        return 0

    current = numbers[i]
    dont_take_current = _max_increasing_subseq(numbers, i + 1, previous, memo)
    options = [dont_take_current]

    if current > previous:
        take_current = 1 + _max_increasing_subseq(numbers, i + 1, current, memo)
        options.append(take_current)

    memo[key] = max(options)
    return memo[key]


def max_increasing_subseq_iter(numbers: list[int]) -> int:
    memo = defaultdict(int)
    n = len(numbers)

    for i in range(n - 1, -1, -1):
        current = numbers[i]
        i_key = (i, current)

        max_subseq = 0

        for j in range(i + 1, n):
            j_key = (j, numbers[j])

            if numbers[j] > current:
                max_subseq = max(max_subseq, memo[j_key])
        memo[i_key] = max_subseq + 1

    return max(memo.values())
