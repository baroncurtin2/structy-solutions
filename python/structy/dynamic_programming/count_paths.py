OPEN = "O"
WALL = "X"


def count_paths(grid: list[list[str]]) -> int:
    # r = # rows
    # c = # columns
    # Time: O(r*c)
    # Space: O(r*c)
    return _count_paths(grid, 0, 0, {})


def _count_paths(grid: list[list[str]], row: int, col: int, memo: dict) -> int:
    pos = (row, col)
    end = (len(grid) - 1, len(grid[0]) - 1)

    if pos in memo:
        return memo[pos]

    if not _inbounds(grid, row, col) or _hit_wall(grid, row, col):
        return 0

    if pos == end:
        return 1

    down_count = _count_paths(grid, row + 1, col, memo)
    right_count = _count_paths(grid, row, col + 1, memo)
    memo[pos] = down_count + right_count
    return memo[pos]


def _inbounds(grid: list[list[str]], row: int, col: int) -> bool:
    row_in = 0 <= row < len(grid)
    col_in = 0 <= col < len(grid[0])
    return row_in and col_in


def _hit_wall(grid: list[list[str]], row: int, col: int) -> bool:
    return grid[row][col] == WALL
