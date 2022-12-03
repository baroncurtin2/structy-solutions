from .common import Node, NodeValue


def tree_sum_iter(root: Node) -> int:
    # Time: O(n)
    # Space: O(n)
    if not root:
        return 0

    stack = [root]
    total = 0

    while stack:
        node = stack.pop()
        total += node.val

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return total


def tree_sum_recur(root: Node) -> int:
    # Time: O(n)
    # Space: O(n)
    return root.val + tree_sum_recur(root.left) + tree_sum_recur(root.right) if root else 0
