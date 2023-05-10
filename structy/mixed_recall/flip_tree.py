import copy
from typing import Optional

from structy.mixed_recall.common import BinaryTreeNode


def flip_tree(root: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # n = number of nodes
    # h = height of the tree
    # Time: O(n)
    # Space: O(h)
    if not root:
        return None

    root_ = copy.deepcopy(root)
    left = flip_tree(root_.left)
    right = flip_tree(root_.right)

    root_.left, root_.right = right, left

    return root_


def flip_tree_iter(root: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if not root:
        return None

    root_ = copy.deepcopy(root)
    stack = [root_]

    while stack:
        current = stack.pop()
        current.left, current.right = current.right, current.left

        if current.left:
            stack = [*stack, current.left]
        if current.right:
            stack = [*stack, current.right]

    return root_
