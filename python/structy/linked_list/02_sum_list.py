from .common import Node


def sum_list_iter(head: Node) -> int:
    # Time: O(n)
    # Space: O(1)
    current = head
    total = 0

    while current is not None:
        total += current.val
        current = current.next

    return total


def sum_list_recur(head: Node) -> int:
    # Time: O(n)
    # Space: O(n)
    if head is None:
        return 0
    return head.val + sum_list_recur(head.next)
