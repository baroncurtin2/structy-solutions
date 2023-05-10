from .common import Node, NodeValue


def tree_includes_iter(root: Node, target: NodeValue) -> bool:
    # Time: O(n)
    # Space: O(n)
    if not root:
        return False

    stack = [root]

    while stack:
        node = stack.pop()

        if node.val == target:
            return True

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return False


def tree_includes_recur(root: Node, target: NodeValue) -> bool:
    # Time: O(n)
    # Space: O(n)
    if not root:
        return False

    if root.val == target:
        return True

    return tree_includes_recur(root.left, target) or tree_includes_recur(root.right, target)
