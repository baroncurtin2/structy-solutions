from dataclasses import dataclass

import pytest

from structy.dynamic_programming.max_path_sum import Grid, max_path_sum


@dataclass(slots=True)
class MaxPathSumTestCase:
    grid: Grid
    expected: int


@pytest.fixture
def test_cases() -> list[MaxPathSumTestCase]:
    return [
        MaxPathSumTestCase(
            grid=[
                [1, 3, 12],
                [5, 1, 1],
                [3, 6, 1],
            ],
            expected=18,
        ),
        MaxPathSumTestCase(
            grid=[
                [1, 3, 12],
                [5, 1, 1],
                [3, 6, 1],
            ],
            expected=18,
        ),
        MaxPathSumTestCase(
            grid=[
                [1, 3, 12],
                [5, 1, 1],
                [3, 6, 1],
            ],
            expected=18,
        ),
        MaxPathSumTestCase(
            grid=[
                [1, 3, 12],
                [5, 1, 1],
                [3, 6, 1],
            ],
            expected=18,
        ),
        MaxPathSumTestCase(
            grid=[
                [1, 3, 12],
                [5, 1, 1],
                [3, 6, 1],
            ],
            expected=18,
        ),
    ]


def test_max_path_sum(test_cases):
    for t in test_cases:
        assert max_path_sum(t.grid) == t.expected
