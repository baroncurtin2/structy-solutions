from .common import Node


def linked_list_find_iter(head: Node, target: str) -> bool:
    # Time: O(n)
    # Space: O(1)
    current = head

    while current is not None:
        if current.val == target:
            return True

        current = current.next

    return False


def linked_list_find_recur(head: Node, target: str) -> bool:
    # Time: O(n)
    # Space: O(n)
    if head is None:
        return False
    if head.val == target:
        return True
    return linked_list_find_recur(head.next, target)
