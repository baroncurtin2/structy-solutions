from structy.mixed_recall.common import Node


def linked_palindrome(head: Node) -> bool:
    values = []
    current = head

    while current:
        values.append(current.val)
        current = current.next

    return values == values[::-1]
