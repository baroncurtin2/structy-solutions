from .common import Node


def insert_node_iter(head: Node, value: str, index: int) -> Node:
    # Time: O(n)
    # Space: O(1)
    if index == 0:
        new_node = Node(value)
        new_node.next = head
        return new_node

    count = 0
    current = head

    while current is not None:
        if count == index - 1:
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node
            break

        current = current.next
        count += 1

    return head


def insert_node_recur(head: Node, value: str, index: int) -> Node:
    # Time: O(n)
    # Space: O(n)
    if index == 0:
        new_head = Node(value)
        new_head.next = head
        return new_head

    _insert_node_recur(head, value, index, 0)
    return head


def _insert_node_recur(node: Node, value: str, index: int, count: int) -> Node:
    if node is None:
        return None

    if count == index - 1:
        temp = node.next
        head.next = Node(value)
        head.next.next = temp
        return

    _insert_node_recur(node.next, value, index, count + 1)
