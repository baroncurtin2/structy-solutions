from collections import Counter


def anagrams_dict(s1: str, s2: str) -> bool:
    # Time: O(n + m)
    # Space: O(n + m)
    if len(s1) != len(s2):
        return False

    def count_characters(s):
        counts = {}

        for c in s:
            counts[c] = counts.setdefault(c, 0) + 1

        return counts

    return count_characters(s1) == count_characters(s2)


def anagrams_counter(s1: str, s2: str) -> bool:
    # Time: O(n + m)
    # Space: O(n + m)
    return Counter(s1) == Counter(s2)
