from structy.mixed_recall.common import BinaryTreeNode


def build_tree_in_pre(in_order: list[str], pre_order: list[str]) -> BinaryTreeNode:
    # n = length of array
    # Time: O(n^2)
    # Space: O(n^2)
    return _build_tree_in_pre(in_order, pre_order, 0, len(in_order) - 1, 0, len(pre_order) - 1)


def _build_tree_in_pre(
    in_order: list[str], pre_order: list[str], start_in: int, end_in: int, start_pre: int, end_pre: int
) -> BinaryTreeNode:
    if end_in < start_in:
        return None

    val = pre_order[start_pre]
    root = BinaryTreeNode(val)
    mid = in_order.index(val)
    left_size = mid - start_in

    root.left = _build_tree_in_pre(in_order, pre_order, start_in, mid - 1, start_pre + 1, start_pre + left_size)
    root.right = _build_tree_in_pre(in_order, pre_order, mid + 1, end_in, start_pre + left_size + 1, end_pre)

    return root
