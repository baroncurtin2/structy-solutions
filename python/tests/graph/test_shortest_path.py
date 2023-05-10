from dataclasses import dataclass

import pytest

from structy.graph.common import NodeValue
from structy.graph.shortest_path import shortest_path


@dataclass(slots=True)
class ShortestPathTestCase:
    edges: list[list]
    node_a: NodeValue
    node_b: NodeValue
    expected: int


@pytest.fixture
def test_cases() -> list[ShortestPathTestCase]:
    return [
        ShortestPathTestCase(
            edges=[["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]],
            node_a="w",
            node_b="z",
            expected=2,
        ),
        ShortestPathTestCase(
            edges=[["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]],
            node_a="y",
            node_b="x",
            expected=1,
        ),
        ShortestPathTestCase(
            edges=[["a", "c"], ["a", "b"], ["c", "b"], ["c", "d"], ["b", "d"], ["e", "d"], ["g", "f"]],
            node_a="a",
            node_b="e",
            expected=3,
        ),
        ShortestPathTestCase(
            edges=[["a", "c"], ["a", "b"], ["c", "b"], ["c", "d"], ["b", "d"], ["e", "d"], ["g", "f"]],
            node_a="e",
            node_b="c",
            expected=2,
        ),
        ShortestPathTestCase(
            edges=[["a", "c"], ["a", "b"], ["c", "b"], ["c", "d"], ["b", "d"], ["e", "d"], ["g", "f"]],
            node_a="b",
            node_b="g",
            expected=-1,
        ),
        ShortestPathTestCase(
            edges=[["c", "n"], ["c", "e"], ["c", "s"], ["c", "w"], ["w", "e"]],
            node_a="w",
            node_b="e",
            expected=1,
        ),
        ShortestPathTestCase(
            edges=[["c", "n"], ["c", "e"], ["c", "s"], ["c", "w"], ["w", "e"]],
            node_a="n",
            node_b="e",
            expected=2,
        ),
        ShortestPathTestCase(
            edges=[["m", "n"], ["n", "o"], ["o", "p"], ["p", "q"], ["t", "o"], ["r", "q"], ["r", "s"]],
            node_a="m",
            node_b="s",
            expected=6,
        ),
    ]


def test_shortest_path(test_cases):
    for tc in test_cases:
        assert shortest_path(tc.edges, tc.node_a, tc.node_b) == tc.expected
