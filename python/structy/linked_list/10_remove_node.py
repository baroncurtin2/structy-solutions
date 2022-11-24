from .common import Node


def remove_node_iter(head: Node, target_val: str) -> Node:
    # Time: O(n)
    # Space: O(1)
    if head.val == target_val:
        return head.next

    current = head
    prev = None

    while current is not None:
        if current.val == target_val:
            prev.next = current.next
            break

        prev = current
        current = current.next
    return head


def remove_node_recur(head: Node, target_val: str) -> Node:
    # Time: O(n)
    # Space: O(n)
    if head is None:
        return None

    if head.val == target_val:
        return head.next

    head.next = remove_node_recur(head.next, target_val)
    return head
