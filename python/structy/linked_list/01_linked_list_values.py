from .common import Node


def linked_list_values_iter(head: Node) -> list[str]:
    # Time: O(n)
    # Space: O(n)
    values = []
    current = head

    while current is not None:
        values.append(current.val)
        current = current.next
    return values


def linked_list_values_recursive(head):
    # Time: O(n)
    # Space: O(n)
    values = []
    _linked_list_values(head, values)

    return values


def _linked_list_values(node, values):
    if node is None:
        return

    values.append(node.val)
    _linked_list_values(node.next, values)
