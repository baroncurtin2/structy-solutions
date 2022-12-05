from dataclasses import dataclass


import pytest

from structy.graph.shortest_path import shortest_path_bfs, shortest_path_recur,shortest_path_dfs


@dataclass
class ShortestPathTestCase:
    edges: list[list]
    expected: int


@pytest.fixture
def test_cases() -> list[ShortestPathTestCase]:
    return [
        ShortestPathTestCase(
            edges=[],
            expected=2,
        ),
        ShortestPathTestCase(
            edges=[],
            expected=2,
        ),
        ShortestPathTestCase(
            edges=[],
            expected=2,
        ),
        ShortestPathTestCase(
            edges=[],
            expected=2,
        ),
        ShortestPathTestCase(
            edges=[],
            expected=2,
        ),
    ]