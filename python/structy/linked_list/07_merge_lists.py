from .common import Node


def merge_lists_iter(head_1: Node, head_2: Node) -> None:
    # Time: O(min(n, m))
    # Space: O(1)
    dummy = Node(None)
    tail = dummy

    current_1 = head_1
    current_2 = head_2

    while current_1 is not None and current_2 is not None:
        if current_1.val < current_2.val:
            tail.next = current_1
            current_1 = current_1.next
        else:
            tail.next = current_2
            current_2 = current_2.next

        tail = tail.next

    tail.next = next((node for node in [current_1, current_2] if node is not None))
    return dummy.next


def merge_lists_recur(head_1: Node, head_2: Node) -> None:
    # Time: O(min(n, m))
    # Space: O(min(n, m))
    if head_1 is None and head_2 is None:
        return None


def _merge_lists_recur(node_1: Node, node_2: Node) -> Node:
    if node_1 is None:
        return node_2
    if node_2 is None:
        return node_1

    if node_1.val < node_2.val:
        next_1 = node_1.next
        node_1.next = _merge_lists_recur(next_1, node_2)
        return node_1
    else:
        next_2 = node_2.next
        node_2.next = _merge_lists_recur(node_1, next_2)
        return head_2
