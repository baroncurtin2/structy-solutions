from structy.graph.common import Grid

from collections import deque

CARROT = "C"
WALL = "X"
OPEN = "O"


def closest_carrot(grid: Grid, starting_row: int, starting_col: int) -> int:
    if not grid:
        return -1

    visited = {(starting_row, starting_col)}
    queue = deque([(starting_row, starting_col, 0)])

    while queue:
        row, col, distance = queue.popleft()

        if grid[row][col] == CARROT:
            return distance

        for x in [-1, 1]:
            # vertical move
            pos = (row + x, col)
            _move(grid, pos, distance, visited, queue)

            # horizontal move
            pos = (row, col + x)
            _move(grid, pos, distance, visited, queue)

    return -1


def _move(grid: Grid, pos: tuple[int, int], distance: int, visited: set, queue: deque) -> None:
    if _inbounds(grid, pos[0], pos[1]) and pos not in visited and not _is_wall(grid, pos[0], pos[1]):
        visited.add(pos)
        queue.append((pos[0], pos[1], distance + 1))


def _inbounds(grid: Grid, row: int, col: int) -> bool:
    row_in = 0 <= row < len(grid)
    col_in = 0 <= col < len(grid[0])

    return row_in & col_in


def _is_wall(grid: Grid, row: int, col: int) -> bool:
    return grid[row][col] == WALL
