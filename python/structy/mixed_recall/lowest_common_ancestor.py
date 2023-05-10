from typing import Optional

from structy.mixed_recall.common import BinaryTreeNode, NodeValue


def lowest_common_ancestor(root: BinaryTreeNode, val1: NodeValue, val2: NodeValue) -> NodeValue:
    # n = number of nodes
    # Time: O(n)
    # Space: O(n)
    path1 = find_path(root, val1)
    path2 = find_path(root, val2)
    set2 = set(path2)

    for val in path1:
        if val in set2:
            return val


def find_path(root: NodeValue, target: NodeValue) -> Optional[list[NodeValue]]:
    if not root:
        return None

    if root.val == target:
        return [root.val]

    if left_path := find_path(root.left, target):
        left_path.append(root.val)
        return left_path

    if right_path := find_path(root.right, target):
        right_path.append(root.val)
        return right_path

    return None
