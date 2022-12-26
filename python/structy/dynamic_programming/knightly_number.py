def knightly_number(n: int, m: int, kr: int, kc: int, pr: int, pc: int) -> int:
    """

    :param n: the length of the chess board
    :param m: the number of moves that must be used
    :param kr: the starting row of the knight
    :param kc: the starting column of the knight
    :param pr: the target row
    :param pc: the target column
    :return: the number of different ways the knight can move to the target in exactly m moves
    """
    return _knightly_number(n, m, kr, kc, pr, pc, {})


def _knightly_number(n: int, m: int, kr: int, kc: int, pr: int, pc: int, memo: dict) -> int:
    key = (m, kr, kc)

    if key in memo:
        return memo[key]

    if m == 0:
        knight_pos = (kr, kc)
        pawn_pos = (pr, pc)

        return 1 if knight_pos == pawn_pos else 0

    count = 0
    for next_move in valid_knight_moves(n, kr, kc):
        r_next, c_next = next_move
        count += _knightly_number(n, m - 1, r_next, c_next, pr, pc, memo)

    memo[key] = count
    return count


def _inbounds(n, row, col) -> bool:
    row_in = 0 <= row < n
    col_in = 0 <= col < n
    return row_in and col_in


def valid_knight_moves(n: int, r: int, c: int) -> list[tuple[int, int]]:
    next_positions = [
        (r + 2, c + 1),
        (r + 2, c - 1),
        (r - 2, c + 1),
        (r - 2, c - 1),
        (r + 1, c + 2),
        (r + 1, c - 2),
        (r - 1, c + 2),
        (r - 1, c - 2),
    ]

    return [(row, col) for (row, col) in next_positions if _inbounds(n, row, col)]
