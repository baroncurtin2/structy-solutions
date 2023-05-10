from collections import Counter


def most_frequent_char_dict(s: str) -> str:
    # Time: O(n)
    # Space: O(n)
    counts = count_characters(s)
    max_value = 0
    max_value_char = None

    for c in s:
        val = counts[c]

        if val > max_value:
            max_value = val
            max_value_char = c

    return max_value_char


def count_characters(s: str) -> dict[str, int]:
    counts = {}

    for c in s:
        counts[c] = counts.setdefault(c, 0) + 1
    return counts


def most_frequent_char_counter(s: str) -> str:
    # Time: O(n)
    # Space: O(n)
    counts = Counter(s)
    return max(counts, key=counts.get)
