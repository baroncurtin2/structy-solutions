from dataclasses import dataclass

import pytest

from structy.graph.has_cycle import has_cycle_dfs_iter, has_cycle_recur


@dataclass(slots=True)
class HasCycleTestCase:
    adj_list: dict[str, list[str]]
    expected: bool


@pytest.fixture
def test_cases() -> list[HasCycleTestCase]:
    return [
        HasCycleTestCase(
            adj_list={
                "a": ["b"],
                "b": ["c"],
                "c": ["a"],
            },
            expected=True,
        ),
        HasCycleTestCase(
            adj_list={
                "a": ["b", "c"],
                "b": ["c"],
                "c": ["d"],
                "d": [],
            },
            expected=False,
        ),
        HasCycleTestCase(
            adj_list={
                "a": ["b", "c"],
                "b": [],
                "c": [],
                "e": ["f"],
                "f": ["e"],
            },
            expected=True,
        ),
        HasCycleTestCase(
            adj_list={
                "q": ["r", "s"],
                "r": ["t", "u"],
                "s": [],
                "t": [],
                "u": [],
                "v": ["w"],
                "w": [],
                "x": ["w"],
            },
            expected=False,
        ),
        HasCycleTestCase(
            adj_list={
                "a": ["b"],
                "b": ["c"],
                "c": ["a"],
                "g": [],
            },
            expected=True,
        ),
        HasCycleTestCase(
            adj_list={
                "a": ["b"],
                "b": ["c"],
                "c": ["d"],
                "d": ["b"],
            },
            expected=True,
        ),
    ]


def test_has_cycle_dfs_iter(test_cases):
    for t in test_cases:
        assert has_cycle_dfs_iter(t.adj_list) == t.expected


def test_has_cycle_recur(test_cases):
    for t in test_cases:
        assert has_cycle_recur(t.adj_list) == t.expected
