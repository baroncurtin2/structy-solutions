from dataclasses import dataclass

import pytest

from structy.graph.common import Graph
from structy.graph.longest_path import longest_path_dfs, longest_path_recur


@dataclass(slots=True)
class LongestPathTestCase:
    graph: Graph
    expected: int


@pytest.fixture
def test_cases() -> list[LongestPathTestCase]:
    return [
        LongestPathTestCase(
            graph={
                "a": ["c", "b"],
                "b": ["c"],
                "c": [],
            },
            expected=2,
        ),
        LongestPathTestCase(
            graph={
                "a": ["c", "b"],
                "b": ["c"],
                "c": [],
                "q": ["r"],
                "r": ["s", "u", "t"],
                "s": ["t"],
                "t": ["u"],
                "u": [],
            },
            expected=4,
        ),
        LongestPathTestCase(
            graph={"h": ["i", "j", "k"], "g": ["h"], "i": [], "j": [], "k": [], "x": ["y"], "y": []},
            expected=2,
        ),
        LongestPathTestCase(
            graph={"a": ["b"], "b": ["c"], "c": [], "e": ["f"], "f": ["g"], "g": ["h"], "h": []},
            expected=3,
        ),
    ]


def test_longest_path_dfs(test_cases):
    for t in test_cases:
        assert longest_path_dfs(t.graph) == t.expected


def test_longest_path_recur(test_cases):
    for t in test_cases:
        assert longest_path_recur(t.graph) == t.expected
