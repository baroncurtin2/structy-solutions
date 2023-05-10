import pytest
from dataclasses import dataclass

from structy.graph.common import Graph
from structy.graph.largest_component import largest_component_bfs, largest_component_recur, largest_component_dfs


@dataclass(slots=True)
class LargestComponentTestCase:
    graph: Graph
    expected: int


@pytest.fixture
def test_cases() -> list[LargestComponentTestCase]:
    return [
        LargestComponentTestCase(
            graph={0: [8, 1, 5], 1: [0], 5: [0, 8], 8: [0, 5], 2: [3, 4], 3: [2, 4], 4: [3, 2]},
            expected=4,
        ),
        LargestComponentTestCase(
            graph={1: [2], 2: [1, 8], 6: [7], 9: [8], 7: [6, 8], 8: [9, 7, 2]},
            expected=6,
        ),
        LargestComponentTestCase(
            graph={3: [], 4: [6], 6: [4, 5, 7, 8], 8: [6], 7: [6], 5: [6], 1: [2], 2: [1]},
            expected=5,
        ),
        LargestComponentTestCase(
            graph={},
            expected=0,
        ),
        LargestComponentTestCase(
            graph={0: [4, 7], 1: [], 2: [], 3: [6], 4: [0], 6: [3], 7: [0], 8: []},
            expected=3,
        ),
    ]


def test_largest_component_bfs(test_cases):
    for tc in test_cases:
        assert largest_component_bfs(tc.graph) == tc.expected


def test_largest_component_dfs(test_cases):
    for tc in test_cases:
        assert largest_component_dfs(tc.graph) == tc.expected


def test_largest_component_recur(test_cases):
    for tc in test_cases:
        assert largest_component_recur(tc.graph) == tc.expected
