from .common import Node


def longest_streak_iter(head: Node) -> int:
    # Time: O(n)
    # Space: O(1)
    max_streak = 0
    current_streak = 0
    prev_val = 0

    current = head

    while current is not None:
        if current.val == prev_val:
            current_streak += 1
        else:
            current_streak = 1

        prev_val = current.val

        if current_streak > max_streak:
            max_streak = current_streak

        current = current.next
    return max_streak