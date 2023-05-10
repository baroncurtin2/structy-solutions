from .common import BinaryTreeNode, NodeValue


def lefty_nodes_recur(root: BinaryTreeNode) -> list[NodeValue]:
    # n = number of nodes
    # Time: O(n)
    # Space: O(n)
    values = []

    traverse(root, 0, values)

    return values


def traverse(root: BinaryTreeNode, level: int, values: list[NodeValue]) -> None:
    if not root:
        return

    # if noe value stored at index 'level'
    if len(values) == level:
        values.append(root.val)

    traverse(root.left, level + 1, values)
    traverse(root.right, level + 1, values)


def lefty_nodes_iter(root: BinaryTreeNode) -> list[NodeValue]:
    # n = number of nodes
    # Time: O(n)
    # Space: O(n)
    if not root:
        return []

    stack = [(root, 0)]
    values = []

    while stack:
        node, level = stack.pop()

        if not node:
            continue
        if len(values) == level:
            values.append(node.val)

        if node.right:
            stack.append((node.right, level + 1))
        if node.left:
            stack.append((node.left, level + 1))
    return values
