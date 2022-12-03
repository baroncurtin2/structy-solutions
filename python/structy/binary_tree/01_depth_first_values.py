from .common import Node, NodeValue


def depth_first_values_iter(root: Node) -> list[NodeValue]:
    # Time: O(n)
    # Space: O(n)

    if not root:
        return []

    stack = [root]
    values = []

    while stack:
        node = stack.pop()
        values.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return values


def depth_first_values_recur(root: Node) -> list[NodeValue]:
    # Time: O(n)
    # Space: O(n)
    if not root:
        return []

    left_values = depth_first_values_recur(root.left)
    right_values = depth_first_values_recur(root.right)
    return [root.val, *left_values, *right_values]
