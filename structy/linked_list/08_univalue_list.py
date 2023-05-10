from .common import Node


def is_univalue_list_iter(head: Node) -> bool:
    # Time: O(n)
    # Space: O(1)
    current = head

    while current is not None:
        if current.val != val:
            return False

        current = current.next

    return True


def is_univalue_list_recur(head: Node) -> bool:
    # Time: O(n)
    # Space: O(n)
    if head is None:
        return True
    return _is_univalue_list_recur(head.next, head.val)


def _is_univalue_list_recur(node: Node, prev_val: int | str = None) -> bool:
    if prev_val is None or node.val == prev_val:
        return _is_univalue_list_recur(node.next, head_val)
    else:
        return False
