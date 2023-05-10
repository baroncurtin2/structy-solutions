from collections import deque

from structy.graph.common import Grid


def island_count_bfs(grid: Grid) -> int:
    # r = number of rows
    # c = number of columns
    # Time: O(rc)
    # Space: O(min(rc))
    if not grid:
        return 0

    lands = {(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "L"}

    count = 0

    while lands:
        count += 1

        row, col = lands.pop()

        connected = deque([(row, col)])

        while connected:
            i, j = connected.popleft()

            for x in [-1, 1]:
                if (i + x, j) in lands:
                    connected.append((i + x, j))
                    lands.remove((i + x, j))

                if (i, j + x) in lands:
                    connected.append((i, j + x))
                    lands.remove((i, j + x))

    return count


def island_count_dfs(grid: Grid) -> int:
    # r = number of rows
    # c = number of columns
    # Time: O(rc)
    # Space: O(min(rc))
    if not grid:
        return 0

    lands = {(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "L"}

    count = 0

    while lands:
        count += 1

        row, col = lands.pop()

        connected = [(row, col)]

        while connected:
            i, j = connected.pop()

            for x in [-1, 1]:
                if (i + x, j) in lands:
                    connected.append((i + x, j))
                    lands.remove((i + x, j))

                if (i, j + x) in lands:
                    connected.append((i, j + x))
                    lands.remove((i, j + x))

    return count


def island_count_recur(grid: Grid) -> int:
    # r = number of rows
    # c = number of columns
    # Time: O(rc)
    # Space: O(rc)
    if not grid:
        return 0

    visited = set()
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if _explore(grid, row, col, visited):
                count += 1

    return count


def _inbounds(grid: Grid, row: int, col: int) -> bool:
    row_in = 0 <= row < len(grid)
    col_in = 0 <= col < len(grid[0])

    return row_in and col_in


def _explore(grid: Grid, row: int, col: int, visited: set) -> bool:
    if not _inbounds(grid, row, col):
        return False

    if grid[row][col] == "W":
        return False

    pos = (row, col)
    if pos in visited:
        return False

    visited.add(pos)

    _explore(grid, row - 1, col, visited)
    _explore(grid, row + 1, col, visited)
    _explore(grid, row, col - 1, visited)
    _explore(grid, row, col + 1, visited)

    return True
