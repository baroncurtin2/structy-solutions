from collections import deque
from typing import Callable

from structy.graph.common import Grid

WATER = "W"
LAND = "L"


def best_bridge(grid: Grid, island_finder: Callable[[Grid, int, int, set], set]) -> int:
    first_island = None

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            potential_island = island_finder(grid, r, c, set())

            if len(potential_island) > 0:
                first_island = potential_island
                break

    visited = set(first_island)
    queue = deque([(r, c, -1) for (r, c) in first_island])

    while queue:
        row, col, distance = queue.popleft()

        if grid[row][col] == LAND and (row, col) not in first_island:
            return distance

        for delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            delta_row, delta_col = delta
            neighbor_row, neighbor_col = row + delta_row, col + delta_col
            neighbor_pos = (neighbor_row, neighbor_col)

            if _inbounds(grid, neighbor_row, neighbor_col) and neighbor_pos not in visited:
                visited.add(neighbor_pos)
                queue.append((neighbor_row, neighbor_col, distance + 1))


def _inbounds(grid: Grid, row: int, col: int):
    row_in = 0 <= row < len(grid)
    col_in = 0 <= col < len(grid[0])
    return row_in and col_in


def find_island_recur(grid: Grid, row: int, col: int, visited: set) -> set:
    if not _inbounds(grid, row, col) or grid[row][col] == WATER:
        return visited

    pos = (row, col)
    if pos in visited:
        return visited

    visited.add(pos)

    for x in [-1, 1]:
        find_island_recur(grid, row + x, col, visited)
        find_island_recur(grid, row, col + x, visited)
    return visited


def find_island_dfs_iter(grid: Grid, row: int, col: int, visited: set) -> set:
    stack = [(row, col)]

    while stack:
        pos = stack.pop()
        x, y = pos

        if not _inbounds(grid, x, y) or grid[x][y] == WATER:
            continue

        if pos in visited:
            continue

        visited.add(pos)
        for delta in [-1, 1]:
            stack.append((x + delta, y))
            stack.append((x, y + delta))

    return visited
