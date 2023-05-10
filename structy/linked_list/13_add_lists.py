from .common import Node


def add_lists_iter(head_1: Node, head_2: Node) -> Node:
    # Time: O(max(n, m))
    # Space: O(max(n, m))
    dummy = Node(None)
    tail = dummy

    carry = 0
    current_1 = head_1
    current_2 = head_2

    while current_1 is not None or current_2 is not None or carry == 1:
        v1 = 0 if current_1 is None else current_1.val
        v2 = 0 if current_2 is None else current_2.val

        add = v1 + v2 + carry
        carry = 1 if add > 9 else 0
        digit = add % 10

        tail.next = Node(digit)
        tail = tail.next

        if current_1 is not None:
            current_1 = current_1.next

        if current_2 is not None:
            current_2 = current_2.next
    return dummy.next


def add_lists_recur(head_1: Node, head_2: Node) -> Node:
    return _add_lists_recur(head_1, head_2, 0)


def _add_lists_recur(node_1: Node, node_2: Node, carry: int) -> Node | None:
    if node_1 is None and node_2 is None and carry == 0:
        return None

    v1 = 0 if node_1 is None else node_1.val
    v2 = 0 if node_2 is None else node_2.val

    add = v1 + v2 + carry
    next_carry = 1 if add > 9 else 0
    digit = add % 10

    result = Node(digit)

    next_1 = None if node_1 is None else node_1.next
    next_2 = None if node_2 is None else node_2.next

    result.next = _add_lists_recur(next_1, next_2, next_carry)
    return result
