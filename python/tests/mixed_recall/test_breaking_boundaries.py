from dataclasses import dataclass

import pytest

from structy.mixed_recall.breaking_boundaries import breaking_boundaries


@dataclass(slots=True)
class BreakingBoundariesTestCase:
    m: int
    n: int
    k: int
    r: int
    c: int
    expected: int


@pytest.fixture
def test_cases() -> list[BreakingBoundariesTestCase]:
    return [
        BreakingBoundariesTestCase(3, 4, 2, 0, 0, expected=4),
        BreakingBoundariesTestCase(2, 2, 2, 1, 1, expected=6),
        BreakingBoundariesTestCase(3, 4, 3, 0, 0, expected=11),
        BreakingBoundariesTestCase(4, 4, 5, 2, 1, expected=160),
        BreakingBoundariesTestCase(5, 6, 9, 2, 5, expected=11635),
        BreakingBoundariesTestCase(6, 6, 12, 3, 4, expected=871065),
        BreakingBoundariesTestCase(6, 6, 15, 3, 4, expected=40787896),
        BreakingBoundariesTestCase(6, 8, 16, 2, 1, expected=137495089),
    ]


def test_breaking_boundaries(test_cases: list[BreakingBoundariesTestCase]) -> None:
    for tc in test_cases:
        assert breaking_boundaries(tc.m, tc.n, tc.k, tc.r, tc.c) == tc.expected
