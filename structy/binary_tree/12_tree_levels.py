from collections import deque

from .common import Node, NodeValue


def tree_levels_iter_bfs(root: Node) -> list[list[NodeValue]]:
    if not root:
        return []

    levels = []
    queue = deque([(root, 0)])

    while queue:
        current, level = queue.popleft()

        if len(levels) == level:
            levels.append([current.val])
        else:
            levels[level].append(current.val)

        if current.left is not None:
            queue.append((current.left, level + 1))
        if current.right is not None:
            queue.append((current.right, level + 1))

    return levels


def tree_levels_recur_dfs(root: Node) -> list[list[NodeValue]]:
    levels = []

    _tree_levels_recur_dfs(root, levels, 0)
    return levels


def _tree_levels_recur_dfs(root: Node, levels: list[list[NodeValue]], level: int) -> None:
    if root is None:
        return

    if level == len(levels):
        levels.append([root.val])
    else:
        levels[level].append(root.val)

    _tree_levels_recur_dfs(root.left, levels, level + 1)
    _tree_levels_recur_dfs(root.right, levels, level + 1)
