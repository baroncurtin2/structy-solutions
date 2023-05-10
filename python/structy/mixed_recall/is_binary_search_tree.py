from structy.mixed_recall.common import BinaryTreeNode


def is_binary_search_tree(root: BinaryTreeNode, recur: bool = False) -> bool:
    if recur:
        return is_binary_search_tree_recur(root)

    return is_binary_search_tree_iter(root)


def is_binary_search_tree_recur(root: BinaryTreeNode) -> bool:
    # n = number of nodes
    # Time: O(n)
    # Space: O(n)
    values = []

    in_order_traversal(root, values)
    return is_sorted(values)


def in_order_traversal(root: BinaryTreeNode, values: list[int]):
    if root is None:
        return

    in_order_traversal(root.left, values)
    values.append(root.val)
    in_order_traversal(root.right, values)


def is_sorted(values: list[int]) -> bool:
    for i in range(len(values) - 1):
        current = values[i]
        next_ = values[i + 1]

        if next_ < current:
            return False

    return True


def is_binary_search_tree_iter(root: BinaryTreeNode) -> bool:
    if not root:
        return False

    prev_val = None
    stack = [root]

    while stack:
        node = stack.pop()

        while node is not None:
            stack.append(node)
            node = node.left

        if not stack:
            break

        node = stack.pop()

        if prev_val is not None and prev_val > node.val:
            return False
        prev_val = node.val

        stack.append(node.right)

    return True
