def befitting_brackets(string: str) -> bool:
    stack = []

    for c in string:
        if c in {"(", "[", "{"}:
            stack.append(_matching_char(c))
        elif stack and stack[-1] == c:
            stack.pop()
        else:
            return False

    return not stack


def _matching_char(char: str) -> str:
    return {
        "(": ")",
        "[": "]",
        "{": "}",
    }.get(char)
