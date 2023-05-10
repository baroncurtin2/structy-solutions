from structy.graph.closest_carrot import closest_carrot

import pytest

from dataclasses import dataclass

from structy.graph.common import Grid


@dataclass(slots=True)
class ClosestCarrotTestCase:
    grid: Grid
    starting_row: int
    starting_col: int
    expected: int


@pytest.fixture
def test_cases() -> list[ClosestCarrotTestCase]:
    return [
        ClosestCarrotTestCase(
            grid=[
                ["O", "O", "O", "O", "O"],
                ["O", "X", "O", "O", "O"],
                ["O", "X", "X", "O", "O"],
                ["O", "X", "C", "O", "O"],
                ["O", "X", "X", "O", "O"],
                ["C", "O", "O", "O", "O"],
            ],
            starting_row=1,
            starting_col=2,
            expected=4,
        ),
        ClosestCarrotTestCase(
            grid=[
                ["O", "O", "O", "O", "O"],
                ["O", "X", "O", "O", "O"],
                ["O", "X", "X", "O", "O"],
                ["O", "X", "C", "O", "O"],
                ["O", "X", "X", "O", "O"],
                ["C", "O", "O", "O", "O"],
            ],
            starting_row=0,
            starting_col=0,
            expected=5,
        ),
        ClosestCarrotTestCase(
            grid=[
                ["O", "O", "X", "X", "X"],
                ["O", "X", "X", "X", "C"],
                ["O", "X", "O", "X", "X"],
                ["O", "O", "O", "O", "O"],
                ["O", "X", "X", "X", "X"],
                ["O", "O", "O", "O", "O"],
                ["O", "O", "C", "O", "O"],
                ["O", "O", "O", "O", "O"],
            ],
            starting_row=3,
            starting_col=4,
            expected=9,
        ),
        ClosestCarrotTestCase(
            grid=[
                ["O", "O", "X", "O", "O"],
                ["O", "X", "X", "X", "O"],
                ["O", "X", "C", "C", "O"],
            ],
            starting_row=1,
            starting_col=4,
            expected=2,
        ),
        ClosestCarrotTestCase(
            grid=[
                ["O", "O", "X", "O", "O"],
                ["O", "X", "X", "X", "O"],
                ["O", "X", "C", "C", "O"],
            ],
            starting_row=2,
            starting_col=0,
            expected=-1,
        ),
        ClosestCarrotTestCase(
            grid=[
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "X", "X"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "X", "C"],
            ],
            starting_row=0,
            starting_col=0,
            expected=-1,
        ),
        ClosestCarrotTestCase(
            grid=[
                ["O", "O", "X", "C", "O"],
                ["O", "X", "X", "X", "O"],
                ["C", "X", "O", "O", "O"],
            ],
            starting_row=2,
            starting_col=2,
            expected=5,
        ),
    ]


def test_closest_carrot(test_cases):
    for t in test_cases:
        assert closest_carrot(t.grid, t.starting_row, t.starting_col) == t.expected
