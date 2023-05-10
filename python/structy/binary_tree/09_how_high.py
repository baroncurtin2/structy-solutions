from .common import Node


def how_high(node: Node) -> int:
    # Time: O(n)
    # Space: O(n)
    if node is None:
        return -1

    left_height = how_high(node.left)
    right_height = how_high(node.right)
    return 1 + max(left_height, right_height)
