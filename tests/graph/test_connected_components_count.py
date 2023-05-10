import pytest
from dataclasses import dataclass

from structy.graph.common import NodeValue
from structy.graph.connected_components_count import (
    connected_components_count_iter_bfs,
    connected_components_count_iter_dfs,
    connected_components_count_recur,
)


@dataclass(slots=True)
class ConnComponentsTestCase:
    graph: dict[NodeValue, list[NodeValue]]
    expected: int


@pytest.fixture
def test_cases() -> list:
    return [
        ConnComponentsTestCase(
            graph={0: [8, 1, 5], 1: [0], 5: [0, 8], 8: [0, 5], 2: [3, 4], 3: [2, 4], 4: [3, 2]},
            expected=2,
        ),
        ConnComponentsTestCase(
            graph={1: [2], 2: [1, 8], 6: [7], 9: [8], 7: [6, 8], 8: [9, 7, 2]},
            expected=1,
        ),
        ConnComponentsTestCase(
            graph={3: [], 4: [6], 6: [4, 5, 7, 8], 8: [6], 7: [6], 5: [6], 1: [2], 2: [1]},
            expected=3,
        ),
        ConnComponentsTestCase(
            graph={},
            expected=0,
        ),
        ConnComponentsTestCase(
            graph={0: [4, 7], 1: [], 2: [], 3: [6], 4: [0], 6: [3], 7: [0], 8: []},
            expected=5,
        ),
    ]


def test_connected_components_count_iter_bfs(test_cases):
    for test_case in test_cases:
        assert connected_components_count_iter_bfs(test_case.graph) == test_case.expected


def test_connected_components_count_iter_dfs(test_cases):
    for test_case in test_cases:
        assert connected_components_count_iter_dfs(test_case.graph) == test_case.expected


def test_connected_components_count_recur(test_cases):
    for test_case in test_cases:
        assert connected_components_count_recur(test_case.graph) == test_case.expected
