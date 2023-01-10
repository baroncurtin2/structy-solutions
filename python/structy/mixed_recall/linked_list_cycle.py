from .common import LinkedList, NodeValue, Node


def linked_list_cycle(head: Node) -> bool:
    # n = number of nodes
    # Time: O(n)
    # Space: O(n)
    visited = set()

    current = head

    while current:
        if (val := current.val) in visited:
            return True
        visited.add(val)
        current = current.next

    return False


def linked_list_cycle_pointers(head: Node) -> bool:
    # n = number of nodes
    # Time: O(n)
    # Space: O(1)

    first_iteration = True
    slow = head
    fast = head

    while fast and fast.next:
        if slow is fast and not first_iteration:
            return True

        first_iteration = False
        slow = slow.next
        fast = fast.next.next

    return False
