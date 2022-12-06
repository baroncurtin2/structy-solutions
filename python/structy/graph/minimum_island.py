from collections import deque
from structy.graph.common import Grid


def minimum_island_bfs(grid: Grid) -> int:
    # r = number of rows
    # c = number of columns
    # Time: O(rc)
    # Space: O(min(rc))
    if not grid:
        return 0

    min_size = float("inf")
    lands = {(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "L"}

    while lands:
        row, col = lands.pop()
        connected = deque([(row, col)])
        size = 1

        while connected:
            i, j = connected.popleft()

            for x in [-1, 1]:
                if (i + x, j) in lands:
                    size += 1
                    connected.append((i + x, j))
                    lands.remove((i + x, j))

                if (i, j + x) in lands:
                    size += 1
                    connected.append((i, j + x))
                    lands.remove((i, j + x))

        min_size = min(size, min_size)

    return min_size


def minimum_island_dfs(grid: Grid) -> int:
    # r = number of rows
    # c = number of columns
    # Time: O(rc)
    # Space: O(min(rc))
    if not grid:
        return 0

    min_size = float("inf")
    lands = {(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "L"}

    while lands:
        row, col = lands.pop()
        connected = [(row, col)]
        size = 1

        while connected:
            i, j = connected.pop()

            for x in [-1, 1]:
                if (i + x, j) in lands:
                    size += 1
                    connected.append((i + x, j))
                    lands.remove((i + x, j))

                if (i, j + x) in lands:
                    size += 1
                    connected.append((i, j + x))
                    lands.remove((i, j + x))

        min_size = min(size, min_size)

    return min_size


def minimum_island_recur(grid: Grid) -> int:
    # r = number of rows
    # c = number of columns
    # Time: O(rc)
    # Space: O(rc)
    visited = set()
    min_size = float("inf")

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = _explore_size(grid, r, c, visited)

            if 0 < size < min_size:
                min_size = size

    return min_size


def _inbounds(grid: Grid, row: int, col: int) -> bool:
    row_in = 0 <= row < len(grid)
    col_in = 0 <= col < len(grid[0])

    return row_in and col_in


def _explore_size(grid: Grid, row: int, col: int, visited: set) -> int:
    if not _inbounds(grid, row, col):
        return 0

    if grid[row][col] == "W":
        return 0

    pos = (row, col)
    if pos in visited:
        return 0

    visited.add(pos)
    size = 1

    for x in [-1, 1]:
        size += _explore_size(grid, row + x, col, visited)
        size += _explore_size(grid, row, col + x, visited)

    return size
