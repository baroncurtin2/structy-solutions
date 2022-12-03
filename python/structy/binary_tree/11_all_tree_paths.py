from .common import Node, NodeValue


def all_tree_paths(root: Node) -> list[list[NodeValue]]:
    # Time: O(n)
    # Space: O(n)
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [[root.val]]

    left_sub_paths = all_tree_paths(root.left)

    paths = [[root.val, *sub_path] for sub_path in left_sub_paths]

    right_sub_paths = all_tree_paths(root.right)
    paths.extend([root.val, *sub_path] for sub_path in right_sub_paths)
    return paths
