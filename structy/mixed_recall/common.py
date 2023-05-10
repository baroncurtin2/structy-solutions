from dataclasses import dataclass, field
from typing import Optional, Self

NodeValue = str | int
UndirectedGraph = dict[str, list[str]]


@dataclass(slots=True)
class LinkedListNode:
    val: NodeValue
    next: "LinkedListNode" = field(default=None, init=False)


@dataclass(slots=True)
class LinkedList:
    head: Optional[LinkedListNode] = None

    def append(self, value: NodeValue) -> None:
        new_node = LinkedListNode(value)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while not current.next:
            current = current.next

        current.next = new_node

    def append_node(self, node: LinkedListNode) -> None:
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
            new_node = LinkedListNode(val)

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


@dataclass(slots=True)
class BinaryTreeNode:
    val: NodeValue
    left: "BinaryTreeNode" = field(default=None, init=False)
    right: "BinaryTreeNode" = field(default=None, init=False)


@dataclass(slots=True)
class BinaryTree:
    root: BinaryTreeNode = None

    def insert(self, value: NodeValue) -> None:
        if not self.root:
            self.root = BinaryTreeNode(value)
            return

        current = self.root

        while current:
            if value < current.val:
                if not current.left:
                    current.left = BinaryTreeNode(value)
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = BinaryTreeNode(value)
                    return
                current = current.right
