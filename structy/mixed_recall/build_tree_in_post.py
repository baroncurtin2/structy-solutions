from structy.mixed_recall.common import BinaryTreeNode


def build_tree_in_post(in_order: list[str], post_order: list[str]) -> BinaryTreeNode:
    # n = length of array
    # Time: O(n^2)
    # Space: O(n^2)
    if not in_order:
        return None

    val = post_order[-1]
    root = BinaryTreeNode(val)
    mid = in_order.index(val)

    left_in_order = in_order[:mid]
    right_in_order = in_order[(mid + 1):]

    left_post_order = post_order[: len(left_in_order)]
    right_post_order = post_order[len(left_in_order): -1]

    root.left = build_tree_in_post(left_in_order, left_post_order)
    root.right = build_tree_in_post(right_in_order, right_post_order)

    return root
