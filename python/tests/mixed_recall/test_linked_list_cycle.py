from dataclasses import dataclass

import pytest

from structy.mixed_recall.common import LinkedList, NodeValue
from structy.mixed_recall.linked_list_cycle import linked_list_cycle, linked_list_cycle_pointers


@dataclass(slots=True)
class LinkedListCycleTestCase:
    values: list[NodeValue] | None
    expected: bool
    cycle: tuple[int, int] = None


@pytest.fixture
def test_cases() -> list[LinkedListCycleTestCase]:
    return [
        LinkedListCycleTestCase(
            values=["a", "b", "c", "d"],
            cycle=(3, 1),
            expected=True,
        ),
        LinkedListCycleTestCase(
            values=["q", "r", "s", "t", "u"],
            cycle=(4, 0),
            expected=True,
        ),
        LinkedListCycleTestCase(
            values=["a", "b", "c", "d"],
            expected=False,
        ),
        LinkedListCycleTestCase(
            values=["q", "r", "s", "t", "u"],
            cycle=(4, 3),
            expected=True,
        ),
        LinkedListCycleTestCase(
            values=["p"],
            expected=False,
        ),
        LinkedListCycleTestCase(
            values=None,
            expected=False,
        ),
    ]


def test_linked_list_cycle(test_cases: list[LinkedListCycleTestCase]) -> None:
    for t in test_cases:
        ll = LinkedList.from_values(t.values, cycle=t.cycle)
        assert linked_list_cycle(ll.head) == t.expected


def test_linked_list_cycle_pointers(test_cases: list[LinkedListCycleTestCase]) -> None:
    for t in test_cases:
        ll = LinkedList.from_values(t.values, cycle=t.cycle)
        assert linked_list_cycle_pointers(ll.head) == t.expected
