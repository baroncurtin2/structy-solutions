def nesting_score(string: str) -> int:
    # n = length of string
    # Time: O(n)
    # Space: O(n)
    stack = [0]

    for c in string:
        if c == "[":
            stack.append(0)
        else:
            popped = stack.pop()

            stack[-1] += 1 if popped == 0 else popped * 2

    return stack[0]
