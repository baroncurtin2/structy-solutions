from structy.mixed_recall.common import LinkedListNode


def linked_palindrome(head: LinkedListNode) -> bool:
    values = []
    current = head

    while current:
        values.append(current.val)
        current = current.next

    return values == values[::-1]
