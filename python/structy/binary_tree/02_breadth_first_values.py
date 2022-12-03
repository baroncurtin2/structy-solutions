from collections import deque

from .common import Node, NodeValue


def breadth_first_values_iter(root: Node) -> list[NodeValue]:
    # Time: O(n)
    # Space: O(n)
    if not root:
        return []

    queue = deque([root])
    values = []

    while queue:
        node = queue.popleft()
        values.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return values
