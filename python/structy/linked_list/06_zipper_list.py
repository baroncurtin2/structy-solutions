from .common import Node


def zipper_lists_iter(head_1: Node, head_2: Node) -> Node:
    # Time: O(min(n, m))
    # Space: O(1)
    count = 0
    tail = head_1
    current_1 = head_1.next
    current_2 = head_2

    while current_1 is not None and current_2 is not None:
        # use first list
        if count % 2 != 0:
            tail.next = current_1
            current_1 = current_1.next
        # use second list
        else:
            tail.next = current_2
            current_2 = current_2.next

        tail = tail.next
        count += 1

    tail.next = next(node for node in [current_1, current_2] if node is not None)
    return head_1


def zipper_lists_recur(head_1: Node, head_2: Node) -> Node:
    # Time: O(min(n, m))
    # Space: O(min(n, m))

    if head_1 is None and head_2 is None:
        return None
    return _zipper_lists_recur(head_1, head_2)


def _zipper_lists_recur(node_1: Node, node_2: Node) -> Node:
    if node_1 is None:
        return node_2
    if node_2 is None:
        return node_1

    next_1 = node_1.next
    next_2 = node_2.next
    node_1.next = node_2
    node_2.next = _zipper_lists_recur(next_1, next_2)
    return node_1
