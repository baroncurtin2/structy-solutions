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

    def append(self, value: NodeValue):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while not current.next:
            current = current.next

        current.next = new_node

    @classmethod
    def from_values(cls, values: list[NodeValue]) -> Self:
        linked_list = LinkedList()

        prev = None

        for val in values:
            new_node = Node(val)

            if prev:
                prev.next = new_node
            else:
                linked_list.head = new_node
            prev = new_node
        return linked_list
