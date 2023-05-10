from .common import Node, NodeValue


def path_finder_inefficient(root: Node, target: NodeValue) -> list[NodeValue]:
    # Time: O(n^2)
    # Space: O(n)
    # sourcery skip: assign-if-exp, reintroduce-else
    if root is None:
        return None

    if root.val == target:
        return [root.val]

    left_path = path_finder_inefficient(root.left, target)

    if left_path is not None:
        return [root.val, *left_path]

    right_path = path_finder_inefficient(root.right, target)
    if right_path is not None:
        return [root.val, *right_path]

    return None


def path_finder_efficient(root: Node, target: NodeValue) -> list[NodeValue]:
    # Time: O(n)
    # Space: O(n)
    result = _path_finder_efficient(root, target)

    return None if result is None else result[::-1]


def _path_finder_efficient(node: Node, target: NodeValue) -> list[NodeValue]:
    if node is None:
        return None

    if node.val == target:
        return [node.val]

    left_path = _path_finder_efficient(node.left, target)

    if left_path is not None:
        left_path.append(node.val)
        return left_path

    right_path = _path_finder_efficient(node.right, target)

    if right_path is not None:
        right_path.append(node.val)
        return right_path
    return None
