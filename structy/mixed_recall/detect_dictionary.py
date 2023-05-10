def detect_dictionary(dictionary: list[str], alphabet: str) -> bool:
    # n = # of words in dictionary
    # k = # length of longest word
    # Time: O(nk)
    # Space: O(1)
    lookup = create_str_lookup_table(alphabet)

    for i in range(len(dictionary) - 1):
        current = dictionary[i]
        next_ = dictionary[i + 1]

        if not lexical_order(current, next_, lookup):
            return False

    return True


def create_str_lookup_table(alphabet: str) -> dict[str, int]:
    return {char: i for i, char in enumerate(alphabet)}


def lexical_order(word_1: str, word_2: str, lookup: dict[str, int]) -> bool:
    max_len = max(len(word_1), len(word_2))

    for i in range(max_len):
        if i >= len(word_1) or i >= len(word_2):
            return len(word_1) <= len(word_2)

        value_1 = lookup.get(word_1[i])
        value_2 = lookup.get(word_2[i])

        if value_1 != value_2:
            return value_1 < value_2

    return True
