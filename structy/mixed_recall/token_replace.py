def token_replace(s: str, tokens: dict[str, str]) -> str:
    # n = length of string
    # Time: O(n)
    # Space: O(n)
    i = 0
    j = 1

    result = []

    while i < len(s):
        if s[i] != "$":
            result.append(s[i])
            i += 1
            j = i + 1
        elif s[j] != "$":
            j += 1
        else:
            key = s[i: j + 1]
            result.append(tokens[key])
            i = j + 1
            j = i + 1

    return "".join(result)
