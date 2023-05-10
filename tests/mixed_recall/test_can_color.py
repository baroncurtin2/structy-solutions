from dataclasses import dataclass

import pytest

from structy.mixed_recall.can_color import can_color
from structy.mixed_recall.common import UndirectedGraph


@dataclass(slots=True)
class CanColorTestCase:
    graph: UndirectedGraph
    expected: bool


@pytest.fixture
def test_cases() -> list[CanColorTestCase]:
    return [
        CanColorTestCase(
            graph={"x": ["y"], "y": ["x", "z"], "z": ["y"]},
            expected=True,
        ),
        CanColorTestCase(
            graph={"q": ["r", "s"], "r": ["q", "s"], "s": ["r", "q"]},
            expected=False,
        ),
        CanColorTestCase(
            graph={
                "a": ["b", "c", "d"],
                "b": ["a"],
                "c": ["a"],
                "d": ["a"],
            },
            expected=True,
        ),
        CanColorTestCase(
            graph={
                "a": ["b", "c", "d"],
                "b": ["a"],
                "c": ["a", "d"],
                "d": ["a", "c"],
            },
            expected=False,
        ),
        CanColorTestCase(
            graph={
                "h": ["i", "k"],
                "i": ["h", "j"],
                "j": ["i", "k"],
                "k": ["h", "j"],
            },
            expected=True,
        ),
        CanColorTestCase(
            graph={"z": []},
            expected=True,
        ),
        CanColorTestCase(
            graph={
                "h": ["i", "k"],
                "i": ["h", "j"],
                "j": ["i", "k"],
                "k": ["h", "j"],
                "q": ["r", "s"],
                "r": ["q", "s"],
                "s": ["r", "q"],
            },
            expected=False,
        ),
        CanColorTestCase(
            graph={
                "a": ["b", "d"],
                "c": ["b", "f"],
                "b": ["a", "c"],
                "d": ["a", "e"],
                "e": ["d", "f"],
                "f": ["e", "c"],
            },
            expected=True,
        ),
    ]


def test_can_color(test_cases) -> None:
    for tc in test_cases:
        assert can_color(tc.graph, recur=False) == tc.expected
        assert can_color(tc.graph, recur=True) == tc.expected
