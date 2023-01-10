from dataclasses import dataclass, field
from typing import Optional, Self

NodeValue = str | int


@dataclass(slots=True)
class Node:
    val: NodeValue
    next: "Node" = field(default=None, init=False)


@dataclass(slots=True)
class LinkedList:
    head: Optional[Node] = None

    def append(self, value: NodeValue) -> None:
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while not current.next:
            current = current.next

        current.next = new_node

    def append_node(self, node: Node) -> None:
        if not self.head:
            self.head = node
            return

        current = self.head
        while not current.next:
            current = current.next

        current.next = node

    @classmethod
    def from_values(cls, values: list[NodeValue], cycle: tuple[int, int] = None) -> Self:
        linked_list = cls()

        if not values:
            return linked_list

        if cycle:
            end, start = cycle
        else:
            end, start = None, None
        cycle_start = None
        cycle_end = None

        prev = None

        for i, val in enumerate(values):
            new_node = Node(val)

            if prev:
                prev.next = new_node
            else:
                linked_list.head = new_node
            prev = new_node

            if i == start:
                cycle_start = new_node
            elif i == end:
                cycle_end = new_node

        if cycle:
            cycle_end.next = cycle_start

        return linked_list
