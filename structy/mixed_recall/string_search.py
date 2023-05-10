def string_search(grid: list[list[str]], s: str, recur: bool = False) -> bool:
    return _string_search_recur(grid, s) if recur else _string_search_iter(grid, s)


def _string_search_recur(grid: list[list[str]], s: str) -> bool:
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if dfs(grid, r, c, s, 0):
                return True

    return False


def dfs(grid: list[list[str]], r: int, c: int, s: str, index: int) -> bool:
    if index >= len(s):
        return True

    if not is_inbounds(grid, r, c):
        return False

    if grid[r][c] != s[index]:
        return False

    char = grid[r][c]
    grid[r][c] = "*"

    result = (
        dfs(grid, r - 1, c, s, index + 1)
        or dfs(grid, r + 1, c, s, index + 1)
        or dfs(grid, r, c - 1, s, index + 1)
        or dfs(grid, r, c + 1, s, index + 1)
    )
    grid[r][c] = char

    return result


def _string_search_iter(grid: list[list[str]], s: str) -> bool:
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if dfs_iterative(grid, r, c, s):
                return True

    return False


def dfs_iterative(grid: list[list[str]], r: int, c: int, s: str) -> bool:
    stack = [(r, c, 0)]
    visited = set()

    while stack:
        r, c, index = stack.pop()

        if index >= len(s):
            return True

        if (r, c) in visited or not is_inbounds(grid, r, c) or grid[r][c] != s[index]:
            continue

        visited.add((r, c))

        stack.append((r - 1, c, index + 1))
        stack.append((r + 1, c, index + 1))
        stack.append((r, c - 1, index + 1))
        stack.append((r, c + 1, index + 1))

    return False


def is_inbounds(grid: list[list[str]], r: int, c: int) -> bool:
    row_in = 0 <= r < len(grid)
    col_in = 0 <= c < len(grid[0])
    return row_in and col_in
