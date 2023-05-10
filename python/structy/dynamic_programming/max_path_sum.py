Grid = list[list[int]]


def max_path_sum(grid: Grid) -> int:
    return _max_path_sum(grid, 0, 0, {})


def _max_path_sum(grid: Grid, row: int, col: int, memo: dict) -> int | float:
    pos = (row, col)
    end = (len(grid) - 1, len(grid[0]) - 1)

    if pos in memo:
        return memo[pos]

    if not _inbounds(grid, row, col):
        return float("-inf")

    if pos == end:
        return grid[row][col]

    down = _max_path_sum(grid, row + 1, col, memo)
    right = _max_path_sum(grid, row, col + 1, memo)
    memo[pos] = grid[row][col] + max(down, right)
    return memo[pos]


def _inbounds(grid: Grid, row: int, col: int) -> bool:
    row_in = 0 <= row < len(grid)
    col_in = 0 <= col < len(grid[0])
    return row_in and col_in
