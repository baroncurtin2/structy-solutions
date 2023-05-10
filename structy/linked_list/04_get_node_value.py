from .common import Node


def get_node_value_iter(head: Node, index: int) -> str:
    # Time: O(n)
    # Space: O(1)
    current = head
    cur_i = 0

    while current is not None:
        if cur_i == index:
            return current.val

        current = current.next
        cur_i += 1
    return None


def get_node_value_recur(head: Node, index: int) -> str:
    if head is None:
        return None

    if index == 0:
        return head.val

    return get_node_value_recur(head.next, index - 1)
