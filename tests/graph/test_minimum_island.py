from dataclasses import dataclass

import pytest

from structy.graph.common import Grid
from structy.graph.minimum_island import minimum_island_bfs, minimum_island_dfs, minimum_island_recur


@dataclass(slots=True)
class MinimumIslandTestCase:
    grid: Grid
    expected: int


@pytest.fixture
def test_cases() -> list[MinimumIslandTestCase]:
    return [
        MinimumIslandTestCase(
            grid=[
                ["W", "L", "W", "W", "W"],
                ["W", "L", "W", "W", "W"],
                ["W", "W", "W", "L", "W"],
                ["W", "W", "L", "L", "W"],
                ["L", "W", "W", "L", "L"],
                ["L", "L", "W", "W", "W"],
            ],
            expected=2,
        ),
        MinimumIslandTestCase(
            grid=[
                ["L", "W", "W", "L", "W"],
                ["L", "W", "W", "L", "L"],
                ["W", "L", "W", "L", "W"],
                ["W", "W", "W", "W", "W"],
                ["W", "W", "L", "L", "L"],
            ],
            expected=1,
        ),
        MinimumIslandTestCase(
            grid=[
                ["L", "L", "L"],
                ["L", "L", "L"],
                ["L", "L", "L"],
            ],
            expected=9,
        ),
        MinimumIslandTestCase(
            grid=[["W", "W"], ["L", "L"], ["W", "W"], ["W", "L"]],
            expected=1,
        ),
    ]


def test_minimum_island_bfs(test_cases):
    for t in test_cases:
        assert minimum_island_bfs(t.grid) == t.expected


def test_minimum_island_dfs(test_cases):
    for t in test_cases:
        assert minimum_island_dfs(t.grid) == t.expected


def test_minimum_island_recur(test_cases):
    for t in test_cases:
        assert minimum_island_recur(t.grid) == t.expected
