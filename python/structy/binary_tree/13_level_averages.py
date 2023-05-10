from collections import deque

from .common import Node


def level_averages_iter_bfs(root: Node) -> list[int]:
    # Time: O(n)
    # Space: O(n)
    if not root:
        return []

    levels = []
    queue = deque([(root, 0)])

    while queue:
        node, level = queue.popleft()

        if len(levels) == level:
            levels.append((node.val, 1))
        else:
            total, count = levels[level]
            levels[level] = total + node.val, count + 1

        if node.left is not None:
            queue.append((node.left, level + 1))
        if node.right is not None:
            queue.append((node.right, level + 1))

    return [total / count for (total, count) in levels]


def level_averages_recur(root: Node) -> list[int]:
    # Time: O(n)
    # Space: O(n)
    levels = []
    fill_levels(root, levels, 0)

    return [total / count for (total, count) in levels]


def fill_levels(node: Node, levels: list, level: int) -> None:
    if node is None:
        return

    if level == len(levels):
        levels.append((node.val, 1))
    else:
        total, count = levels[level]
        levels[level] = total + node.val, count + 1

    fill_levels(node.left, levels, level + 1)
    fill_levels(node.right, levels, level + 1)

