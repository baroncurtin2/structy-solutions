from collections import deque

from .common import Node, NodeValue


def tree_value_count_iter(root: Node, target: NodeValue) -> int:
    # depth first search
    # Time: O(n)
    # Space: O(n)
    if root is None:
        return 0

    count = 0
    stack = [root]

    while stack:
        current = stack.pop()

        if current.val == target:
            count += 1

        if current.left is not None:
            stack.append(current.left)
        if current.right is not None:
            stack.append(current.right)
    return count


def tree_value_count_iter2(root: Node, target: NodeValue) -> int:
    # breadth first search
    # Time: O(n)
    # Space: O(n)
    if root is None:
        return 0

    count = 0
    queue = deque([root])

    while queue:
        current = queue.popleft()

        if current.val == target:
            count += 1

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return count


def tree_value_count_recur(root: Node, target: NodeValue) -> int:
    # Time: O(n)
    # Space: O(n)
    if root is None:
        return 0

    match = 1 if root.val == target else 0

    return match + tree_value_count_recur(root.left, target) + tree_value_count_recur(root.right, target)
