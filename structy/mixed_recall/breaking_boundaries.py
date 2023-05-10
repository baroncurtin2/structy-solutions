def breaking_boundaries(m: int, n: int, k: int, r: int, c: int) -> int:
    return _breaking_boundaries(m, n, k, r, c, {})


def _breaking_boundaries(m: int, n: int, k: int, r: int, c: int, memo: dict) -> int:
    key = (k, r, c)

    if key in memo:
        return memo[key]

    if not is_inbounds(m, n, r, c):
        return 1

    if k == 0:
        return 0

    total_count = 0

    for move_fn in move_fns:
        new_k, new_r, new_c = move_fn(k, r, c)
        total_count += _breaking_boundaries(m, n, new_k, new_r, new_c, memo)

    memo[key] = total_count
    return total_count


def is_inbounds(m: int, n: int, r: int, c: int) -> bool:
    is_row_inbounds = 0 <= r < m
    is_col_inbounds = 0 <= c < n

    return is_row_inbounds and is_col_inbounds


def move_up(k: int, r: int, c: int) -> (int, int, int):
    return k - 1, r - 1, c


def move_down(k: int, r: int, c: int) -> (int, int, int):
    return k - 1, r + 1, c


def move_left(k: int, r: int, c: int) -> (int, int, int):
    return k - 1, r, c - 1


def move_right(k: int, r: int, c: int) -> (int, int, int):
    return k - 1, r, c + 1


move_fns = [move_up, move_down, move_left, move_right]
