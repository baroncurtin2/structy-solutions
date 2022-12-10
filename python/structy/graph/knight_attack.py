from collections import deque
from typing import Optional


def knight_attack(n: int, kr: int, kc: int, pr: int, pc: int) -> Optional[int]:
    visited = {(kr, kc)}

    queue = deque([(kr, kc, 0)])

    while queue:
        r, c, moves = queue.popleft()

        if (r, c) == (pr, pc):
            return moves

        for next_move in knight_moves(n, r, c):
            (r2, c2) = next_move

            if next_move not in visited:
                visited.add(next_move)
                queue.append((r2, c2, moves + 1))

    return None


def _inbounds(n: int, row: int, col: int) -> bool:
    row_in = 0 <= row < n
    col_in = 0 <= col < n
    return row_in and col_in


def knight_moves(n: int, r: int, c: int) -> list[tuple[int, int]]:
    positions = [
        (r + 2, c + 1),
        (r + 2, c - 1),
        (r - 2, c + 1),
        (r - 2, c - 1),
        (r + 1, c + 2),
        (r + 1, c - 2),
        (r - 1, c + 2),
        (r - 1, c - 2),
    ]

    return [(row, col) for (row, col) in positions if _inbounds(n, row, col)]
