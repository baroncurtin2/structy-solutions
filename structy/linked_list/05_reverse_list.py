from .common import Node


def reverse_list_iter(head: Node) -> Node:
    # Time: O(n)
    # Space: O(1)
    current = head
    prev = None

    while current is not None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


def reverse_list_recur(head: Node) -> Node:
    # Time: O(n)
    # Space: O(n)
    if head is None:
        return None

    return _reverse_list_recur(head, None)


def _reverse_list_recur(node: Node, prev=None) -> Node:
    nxt = node.next
    node.next = prev
    return _reverse_list_recur(nxt, node)
