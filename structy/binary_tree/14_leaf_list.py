from .common import Node, NodeValue


def leaf_list_iter(root: Node) -> list[NodeValue]:
    # Time: O(n)
    # Space: O(n)
    if not root:
        return []

    stack = [root]
    leaves = []

    while stack:
        node = stack.pop()

        if (not node.left) & (not node.right):
            leaves.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return leaves


def leaf_list_recur(root: Node) -> list[NodeValue]:
    # Time: O(n)
    # Space: O(n)
    leaves = []

    _leaf_list(root, leaves)
    return leaves


def _leaf_list(node: Node, leaves: list[NodeValue]) -> None:
    if not node:
        return

    if (not node.left) & (not node.right):
        leaves.append(node.val)

    _leaf_list(node.left, leaves)
    _leaf_list(node.right, leaves)
