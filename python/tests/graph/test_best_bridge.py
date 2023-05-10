from dataclasses import dataclass

import pytest

from structy.graph.best_bridge import best_bridge, find_island_recur, find_island_dfs_iter
from structy.graph.common import Grid


@dataclass(slots=True)
class BestBridgeTestCase:
    grid: Grid
    expected: int


@pytest.fixture
def test_cases() -> list[BestBridgeTestCase]:
    return [
        BestBridgeTestCase(
            grid=[
                ["W", "W", "W", "L", "L"],
                ["L", "L", "W", "W", "L"],
                ["L", "L", "L", "W", "L"],
                ["W", "L", "W", "W", "W"],
                ["W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W"],
            ],
            expected=1,
        ),
        BestBridgeTestCase(
            grid=[
                ["W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W"],
                ["L", "L", "W", "W", "L"],
                ["W", "L", "W", "W", "L"],
                ["W", "W", "W", "L", "L"],
                ["W", "W", "W", "W", "W"],
            ],
            expected=2,
        ),
        BestBridgeTestCase(
            grid=[
                ["W", "W", "W", "W", "W"],
                ["W", "W", "W", "L", "W"],
                ["L", "W", "W", "W", "W"],
            ],
            expected=3,
        ),
        BestBridgeTestCase(
            grid=[
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "L", "W", "W"],
                ["W", "W", "W", "W", "L", "L", "W", "W"],
                ["W", "W", "W", "W", "L", "L", "L", "W"],
                ["W", "W", "W", "W", "W", "L", "L", "L"],
                ["L", "W", "W", "W", "W", "L", "L", "L"],
                ["L", "L", "L", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
            ],
            expected=3,
        ),
        BestBridgeTestCase(
            grid=[
                ["L", "L", "L", "L", "L", "L", "L", "L"],
                ["L", "W", "W", "W", "W", "W", "W", "L"],
                ["L", "W", "W", "W", "W", "W", "W", "L"],
                ["L", "W", "W", "W", "W", "W", "W", "L"],
                ["L", "W", "W", "W", "W", "W", "W", "L"],
                ["L", "W", "W", "W", "W", "W", "W", "L"],
                ["L", "W", "W", "L", "W", "W", "W", "L"],
                ["L", "W", "W", "W", "W", "W", "W", "L"],
                ["L", "W", "W", "W", "W", "W", "W", "L"],
                ["L", "W", "W", "W", "W", "W", "W", "L"],
                ["L", "W", "W", "W", "W", "W", "W", "L"],
                ["L", "L", "L", "L", "L", "L", "L", "L"],
            ],
            expected=2,
        ),
        BestBridgeTestCase(
            grid=[
                ["W", "L", "W", "W", "W", "W", "W", "W"],
                ["W", "L", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "L", "W"],
                ["W", "W", "W", "W", "W", "W", "L", "L"],
                ["W", "W", "W", "W", "W", "W", "W", "L"],
            ],
            expected=8,
        ),
    ]


def test_best_bridge_recur(test_cases):
    for t in test_cases:
        assert best_bridge(t.grid, find_island_recur) == t.expected


def test_best_bridge_iter(test_cases):
    for t in test_cases:
        assert best_bridge(t.grid, find_island_dfs_iter) == t.expected
