from dataclasses import dataclass

import pytest

from structy.mixed_recall.topological_order import topological_order


@dataclass(slots=True)
class TopologicalOrderTestCase:
    graph: dict[str, list[str]]
    expected: list[str]


@pytest.fixture
def test_cases() -> list[TopologicalOrderTestCase]:
    return [
        TopologicalOrderTestCase(
            graph={
                "a": ["f"],
                "b": ["d"],
                "c": ["a", "f"],
                "d": ["e"],
                "e": [],
                "f": ["b", "e"],
            },
            expected=["c", "a", "f", "b", "d", "e"],
        ),
        TopologicalOrderTestCase(
            graph={
                "h": ["l", "m"],
                "i": ["k"],
                "j": ["k", "i"],
                "k": ["h", "m"],
                "l": ["m"],
                "m": [],
            },
            expected=["j", "i", "k", "h", "l", "m"],
        ),
        TopologicalOrderTestCase(
            graph={
                "q": [],
                "r": ["q"],
                "s": ["r"],
                "t": ["s"],
            },
            expected=["t", "s", "r", "q"],
        ),
        TopologicalOrderTestCase(
            graph={
                "v": ["z", "w"],
                "w": [],
                "x": ["w", "v", "z"],
                "y": ["x"],
                "z": ["w"],
            },
            expected=["y", "x", "v", "z", "w"],
        ),
    ]


def test_topological_order(test_cases: list[TopologicalOrderTestCase]) -> None:
    for tc in test_cases:
        assert topological_order(tc.graph) == tc.expected
