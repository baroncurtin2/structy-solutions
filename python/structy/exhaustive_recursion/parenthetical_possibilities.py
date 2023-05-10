def parenthetical_possibilities(s: str) -> list[str]:
    if not s:
        return [""]

    choices, remainder = get_choices(s)
    return [
        choice + possibility
        for choice in choices
        for possibility in parenthetical_possibilities(remainder)
    ]


def get_choices(s: str) -> (str, str):
    if (char := s[0]) != "(":
        return char, s[1:]

    end = s.index(")")
    return s[1:end], s[end + 1 :]
