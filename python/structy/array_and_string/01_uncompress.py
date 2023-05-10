def uncompress(s: str) -> str:
    # Two pointer solution
    # Time: O(n*m)
    # Space: O(n*m)
    nums = "0123456789"
    result = []

    i, j = 0, 0

    while j < len(s):
        if s[j] in nums:
            j += 1
        else:
            num = int(s[i:j])
            result.append(s[j] * num)

            j += 1
            i = j

    return ''.join(result)
