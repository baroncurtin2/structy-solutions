from .common import Node, NodeValue


def tree_min_value_iter(root: Node) -> NodeValue:
    # Time: O(n)
    # Space: O(n)
    if not root:
        return float("inf")

    stack = [root]
    min_value = float("inf")

    while stack:
        node = stack.pop()
        min_value = min(min_value, node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return min_value


def tree_min_value_recur(root: Node) -> NodeValue:
    # Time: O(n)
    # Space: O(n)
    if root is None:
        return int("inf")

    smallest_left_value = tree_min_value_recur(root.left)
    smallest_right_value = tree_min_value_recur(root.right)
    return min(root.val, smallest_left_value, smallest_right_value)
