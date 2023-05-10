import pytest

from dataclasses import dataclass

from structy.graph.island_count import Grid, island_count_recur, island_count_bfs, island_count_dfs


@dataclass(slots=True)
class IslandCountTestCase:
    grid: Grid
    expected: int


@pytest.fixture
def test_cases() -> list[IslandCountTestCase]:
    return [
        IslandCountTestCase(
            grid=[
                ["W", "L", "W", "W", "W"],
                ["W", "L", "W", "W", "W"],
                ["W", "W", "W", "L", "W"],
                ["W", "W", "L", "L", "W"],
                ["L", "W", "W", "L", "L"],
                ["L", "L", "W", "W", "W"],
            ],
            expected=3,
        ),
        IslandCountTestCase(
            grid=[
                ["L", "W", "W", "L", "W"],
                ["L", "W", "W", "L", "L"],
                ["W", "L", "W", "L", "W"],
                ["W", "W", "W", "W", "W"],
                ["W", "W", "L", "L", "L"],
            ],
            expected=4,
        ),
        IslandCountTestCase(
            grid=[
                ["L", "L", "L"],
                ["L", "L", "L"],
                ["L", "L", "L"],
            ],
            expected=1,
        ),
        IslandCountTestCase(
            grid=[
                ["W", "W"],
                ["W", "W"],
                ["W", "W"],
            ],
            expected=0,
        ),
    ]


def test_island_count_bfs(test_cases):
    for t in test_cases:
        assert island_count_bfs(t.grid) == t.expected


def test_island_count_dfs(test_cases):
    for t in test_cases:
        assert island_count_dfs(t.grid) == t.expected


def test_island_count_recur(test_cases):
    for t in test_cases:
        assert island_count_recur(t.grid) == t.expected
