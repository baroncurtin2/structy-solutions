from .common import Node


def create_linked_list_iter(values: list[str | int]) -> Node:
    # Time: O(n)
    # Space: O(n)
    dummy = Node(None)
    tail = dummy

    for value in values:
        new_node = Node(value)
        tail.next = new_node
        tail = tail.next

    return dummy.next


def create_linked_list_recur(values: list[str | int]) -> Node:
    # Time: O(n)
    # Space: O(n)
    return _create_linked_list_recur(values, 0)


def _create_linked_list_recur(values: list[str | int], i: int) -> Node | None:
    # Time: O(n)
    # Space: O(n)
    if i == len(values):
        return None

    head = Node(values[i])
    head.next = _create_linked_list_recur(values, i + 1)
    return head
