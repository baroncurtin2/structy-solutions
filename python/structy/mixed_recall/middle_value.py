from structy.mixed_recall.common import Node, NodeValue


def middle_value(head: Node) -> NodeValue:
    # n = number of nodes
    # Time: O(n)
    # Space: O(n)
    values = []
    current = head

    while current:
        values.append(current.val)
        current = current.next

    mid = (len(values) + 1) // 2 if len(values) % 2 == 0 else len(values) // 2
    return values[mid]


def middle_value_pointers(head: Node) -> NodeValue:
    # n = number of nodes
    # Time: O(n)
    # Space: O(1)
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow.val
