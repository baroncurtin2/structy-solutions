from .common import BinaryTreeNode


def binary_search_tree_includes(root: BinaryTreeNode, target: int) -> bool:
    # n = number of nodes
    #
    # Worst Case
    #
    # Time: O(n)
    # Space: O(n)
    #
    # Best Case (balanced-tree)
    #
    # Time: O(log(n))
    # Space: O(log(n))
    node = root

    while node:
        if node.val == target:
            return True

        node = node.right if target > node.val else node.left
    return False
