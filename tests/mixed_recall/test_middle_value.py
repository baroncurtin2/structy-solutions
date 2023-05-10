from dataclasses import dataclass

import pytest

from structy.mixed_recall.common import LinkedList, NodeValue
from structy.mixed_recall.middle_value import middle_value, middle_value_pointers


@dataclass(slots=True)
class MiddleValueTestCase:
    values: list[NodeValue]
    expected: NodeValue


@pytest.fixture
def test_cases() -> list[MiddleValueTestCase]:
    return [
        MiddleValueTestCase(
            values=["a", "b", "c", "d", "e"],
            expected="c",
        ),
        MiddleValueTestCase(
            values=["a", "b", "c", "d", "e", "f"],
            expected="d",
        ),
        MiddleValueTestCase(
            values=["x", "y", "z"],
            expected="y",
        ),
        MiddleValueTestCase(
            values=["x", "y"],
            expected="y",
        ),
        MiddleValueTestCase(
            values=["q"],
            expected="q",
        ),
    ]


def test_middle_value(test_cases: list[MiddleValueTestCase]) -> None:
    for t in test_cases:
        ll = LinkedList.from_values(t.values)
        assert middle_value(ll.head) == t.expected


def test_middle_value_pointers(test_cases: list[MiddleValueTestCase]) -> None:
    for t in test_cases:
        ll = LinkedList.from_values(t.values)
        assert middle_value_pointers(ll.head) == t.expected
