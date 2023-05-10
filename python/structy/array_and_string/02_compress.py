def compress(s: str) -> str:
    # Two pointer solution
    # Time: O(n)
    # Space: O(n)
    s += "!"
    result = ""

    i = 0
    j = 0

    while j < len(s):
        if s[i] == s[j]:
            j += 1
            continue

        count = j - i
        result += f"{count if count > 1 else ''}{s[i]}"

        i = j

    return result
