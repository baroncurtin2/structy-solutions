from dataclasses import dataclass

import pytest

from structy.graph.common import NodeValue
from structy.graph.has_path import has_path_bfs_iter, has_path_dfs_iter, has_path_dfs_recur


@dataclass(slots=True)
class HasPathTestCase:
    graph: dict
    src: NodeValue
    dst: NodeValue
    expected: bool


@pytest.fixture
def test_cases():
    return [
        HasPathTestCase(
            graph={"f": ["g", "i"], "g": ["h"], "h": [], "i": ["g", "k"], "j": ["i"], "k": []},
            src="f",
            dst="j",
            expected=False,
        ),
        HasPathTestCase(
            graph={"f": ["g", "i"], "g": ["h"], "h": [], "i": ["g", "k"], "j": ["i"], "k": []},
            src="i",
            dst="h",
            expected=True,
        ),
        HasPathTestCase(
            graph={"v": ["x", "w"], "w": [], "x": [], "y": ["z"], "z": []},
            src="v",
            dst="w",
            expected=True,
        ),
        HasPathTestCase(
            graph={"v": ["x", "w"], "w": [], "x": [], "y": ["z"], "z": []},
            src="v",
            dst="z",
            expected=False,
        ),
    ]


def test_has_path_bfs_iter(test_cases):
    for test_case in test_cases:
        assert has_path_bfs_iter(test_case.graph, test_case.src, test_case.dst) == test_case.expected


def test_has_path_dfs_iter(test_cases):
    for test_case in test_cases:
        assert has_path_dfs_iter(test_case.graph, test_case.src, test_case.dst) == test_case.expected


def test_has_path_dfs_recur(test_cases):
    for test_case in test_cases:
        assert has_path_dfs_recur(test_case.graph, test_case.src, test_case.dst) == test_case.expected
