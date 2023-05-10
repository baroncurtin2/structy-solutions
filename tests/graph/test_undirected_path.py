from dataclasses import dataclass

import pytest

from structy.graph.common import NodeValue
from structy.graph.undirected_path import (
    undirected_path_dfs_iter,
    undirected_path_bfs_iter,
    undirected_path_dfs_recur,
)


@dataclass(slots=True)
class UndirectedPathTest:
    edges: list[tuple]
    node_a: NodeValue
    node_b: NodeValue
    expected: bool


@pytest.fixture
def test_cases() -> list[UndirectedPathTest]:
    return [
        UndirectedPathTest(
            edges=[("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")],
            node_a="j",
            node_b="m",
            expected=True,
        ),
        UndirectedPathTest(
            edges=[("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")],
            node_a="m",
            node_b="j",
            expected=True,
        ),
        UndirectedPathTest(
            edges=[("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")],
            node_a="l",
            node_b="j",
            expected=True,
        ),
        UndirectedPathTest(
            edges=[("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")],
            node_a="k",
            node_b="o",
            expected=False,
        ),
    ]


def test_undirected_path_dfs_recur(test_cases):
    for test_case in test_cases:
        assert undirected_path_dfs_recur(test_case.edges, test_case.node_a, test_case.node_b) == test_case.expected


def test_undirected_path_bfs_iter(test_cases):
    for test_case in test_cases:
        assert undirected_path_bfs_iter(test_case.edges, test_case.node_a, test_case.node_b) == test_case.expected


def test_undirected_path_dfs_iter(test_cases):
    for test_case in test_cases:
        assert undirected_path_dfs_iter(test_case.edges, test_case.node_a, test_case.node_b) == test_case.expected
