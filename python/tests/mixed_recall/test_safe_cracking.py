from dataclasses import dataclass

import pytest

from structy.mixed_recall.safe_cracking import safe_cracking


@dataclass(slots=True)
class SafeCrackingTestCase:
    hints: list[tuple[int, int]]
    expected: str


@pytest.fixture
def test_cases() -> list[SafeCrackingTestCase]:
    return [
        SafeCrackingTestCase(
            hints=[
                (7, 1),
                (1, 8),
                (7, 8),
            ],
            expected="718",
        ),
        SafeCrackingTestCase(
            hints=[
                (3, 1),
                (4, 7),
                (5, 9),
                (4, 3),
                (7, 3),
                (3, 5),
                (9, 1),
            ],
            expected="473591",
        ),
        SafeCrackingTestCase(
            hints=[
                (2, 5),
                (8, 6),
                (0, 6),
                (6, 2),
                (0, 8),
                (2, 3),
                (3, 5),
                (6, 5),
            ],
            expected="086235",
        ),
        SafeCrackingTestCase(
            hints=[
                (0, 1),
                (6, 0),
                (1, 8),
            ],
            expected="6018",
        ),
        SafeCrackingTestCase(
            hints=[
                (8, 9),
                (4, 2),
                (8, 2),
                (3, 8),
                (2, 9),
                (4, 9),
                (8, 4),
            ],
            expected="38429",
        ),
    ]


def test_safe_cracking(test_cases: list[SafeCrackingTestCase]) -> None:
    for tc in test_cases:
        assert safe_cracking(tc.hints) == tc.expected
