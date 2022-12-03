from .common import Node


def max_path_sum(root: Node) -> int | float:
    # Time: O(n)
    # Space: O(n)

    if root is None:
        return float("-inf")

    if root.left is None and root.right is None:
        return root.val

    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))
