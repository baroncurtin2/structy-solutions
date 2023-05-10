def paired_parentheses(string: str) -> bool:
    count = 0

    for c in string:
        if c == "(":
            count += 1
        elif c == ")":
            if count == 0:
                return False
            count -= 1

    return count == 0
