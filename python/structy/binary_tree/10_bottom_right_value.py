from collections import deque

from .common import Node, NodeValue


def bottom_right_value(root: Node) -> NodeValue:
    # Time: O(n)
    # Space: O(n)
    if root is None:
        return None

    queue = deque([root])
    node = None

    while queue:
        node = queue.popleft()

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return node.val
