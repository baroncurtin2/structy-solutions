from collections import deque


def decompress_braces(string: str) -> str:
    stack = []

    for c in string:
        if c.isnumeric():
            stack.append(int(c))
        elif c == "}":
            # popping subroutine
            stack.append(_decompress(stack))
        elif c != "{":
            stack.append(c)

    return "".join(stack)


def _decompress(stack: list) -> str:
    str_segment = deque()

    while type(stack[-1]) is not int:
        char = stack.pop()
        str_segment.appendleft(char)

    # top of stack must be a number
    number = stack.pop()
    return "".join(str_segment) * number
