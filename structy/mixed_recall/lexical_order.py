def lexical_order(word_1: str, word_2: str, alphabet: str) -> bool:
    # n = length of shorter string
    # Time: O(n)
    # Space: O(1)
    max_len = max(len(word_1), len(word_2))

    for i in range(max_len):
        if i >= len(word_1) or i >= len(word_2):
            return len(word_1) <= len(word_2)

        value_1 = alphabet.index(word_1[i])
        value_2 = alphabet.index(word_2[i])

        if value_1 != value_2:
            return value_1 < value_2

    return True
