from dataclasses import dataclass

import pytest

from structy.mixed_recall.combine_intervals import combine_intervals


@dataclass(slots=True)
class CombineIntervalsTestCase:
    intervals: list[tuple[int, int]]
    expected: list[tuple[int, int]]


@pytest.fixture
def test_cases() -> list[CombineIntervalsTestCase]:
    return [
        CombineIntervalsTestCase(
            intervals=[
                (1, 4),
                (12, 15),
                (3, 7),
                (8, 13),
            ],
            expected=[
                (1, 7),
                (8, 15),
            ],
        ),
        CombineIntervalsTestCase(
            intervals=[
                (6, 8),
                (2, 9),
                (10, 12),
                (20, 24),
            ],
            expected=[
                (2, 9),
                (10, 12),
                (20, 24),
            ],
        ),
        CombineIntervalsTestCase(
            intervals=[
                (3, 7),
                (5, 8),
                (1, 5),
            ],
            expected=[(1, 8)],
        ),
        CombineIntervalsTestCase(
            intervals=[
                (3, 7),
                (10, 13),
                (5, 8),
                (27, 31),
                (1, 5),
                (12, 16),
                (20, 22),
            ],
            expected=[
                (1, 8),
                (10, 16),
                (20, 22),
                (27, 31),
            ],
        ),
        CombineIntervalsTestCase(
            intervals=[
                (3, 7),
                (10, 13),
                (5, 8),
                (27, 31),
                (1, 5),
                (12, 16),
                (20, 32),
            ],
            expected=[
                (1, 8),
                (10, 16),
                (20, 32),
            ],
        ),
        CombineIntervalsTestCase(
            intervals=[
                (64, 70),
                (50, 55),
                (62, 65),
                (12, 50),
                (72, 300000),
            ],
            expected=[
                (12, 55),
                (62, 70),
                (72, 300000),
            ],
        ),
    ]


def test_combine_intervals(test_cases: list[CombineIntervalsTestCase]) -> None:
    for tc in test_cases:
        assert combine_intervals(tc.intervals) == tc.expected
