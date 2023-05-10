from structy.mixed_recall.common import BinaryTreeNode, NodeValue


def post_order(root: BinaryTreeNode, recur: bool = False) -> list[NodeValue]:
    # n = number of nodes
    # Time: O(n)
    # Space: O(n)
    if not root:
        return []

    return post_order_recur(root) if recur else post_order_iter(root)


def post_order_recur(root: BinaryTreeNode) -> list[NodeValue]:
    values = []
    post_order_traversal(root, values)
    return values


def post_order_traversal(root: BinaryTreeNode, values: list[NodeValue]) -> None:
    if root is None:
        return

    post_order_traversal(root.left, values)
    post_order_traversal(root.right, values)
    values.append(root.val)


def post_order_iter(root: BinaryTreeNode) -> list[NodeValue]:
    values = []

    stack = [(root, False)]

    while stack:
        node, visited = stack.pop()

        if not node:
            continue

        if visited:
            values.append(node.val)
        else:
            stack.append((node, True))

            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))

    return values
