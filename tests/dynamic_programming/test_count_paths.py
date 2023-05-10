from dataclasses import dataclass

import pytest

from structy.dynamic_programming.count_paths import count_paths


@dataclass(slots=True)
class CountPathsTestCase:
    grid: list[list[str]]
    expected: int


@pytest.fixture
def test_cases() -> list[CountPathsTestCase]:
    return [
        CountPathsTestCase(
            grid=[
                ["O", "O"],
                ["O", "O"],
            ],
            expected=2,
        ),
        CountPathsTestCase(
            grid=[
                ["O", "O", "X"],
                ["O", "O", "O"],
                ["O", "O", "O"],
            ],
            expected=5,
        ),
        CountPathsTestCase(
            grid=[
                ["O", "O", "O"],
                ["O", "O", "X"],
                ["O", "O", "O"],
            ],
            expected=3,
        ),
        CountPathsTestCase(
            grid=[
                ["O", "O", "O"],
                ["O", "X", "X"],
                ["O", "O", "O"],
            ],
            expected=1,
        ),
        CountPathsTestCase(
            grid=[
                ["O", "O", "X", "O", "O", "O"],
                ["O", "O", "X", "O", "O", "O"],
                ["X", "O", "X", "O", "O", "O"],
                ["X", "X", "X", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O"],
            ],
            expected=0,
        ),
        CountPathsTestCase(
            grid=[
                ["O", "O", "X", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "X"],
                ["X", "O", "O", "O", "O", "O"],
                ["X", "X", "X", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O"],
            ],
            expected=42,
        ),
        CountPathsTestCase(
            grid=[
                ["O", "O", "X", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "X"],
                ["X", "O", "O", "O", "O", "O"],
                ["X", "X", "X", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "X"],
            ],
            expected=0,
        ),
        CountPathsTestCase(
            grid=[
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ],
            expected=40_116_600,
        ),
        CountPathsTestCase(
            grid=[
                ["O", "O", "X", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "X", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
                ["X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
                ["X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "X", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
                ["X", "X", "X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
                ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
            ],
            expected=3_190_434,
        ),
    ]


def test_count_paths(test_cases):
    for t in test_cases:
        assert count_paths(t.grid) == t.expected
