from dataclasses import dataclass
from typing import Optional

import pytest

from structy.graph.knight_attack import knight_attack


@dataclass(slots=True)
class KnightAttackTestCase:
    func_args: tuple[int, int, int, int, int]
    expected: Optional[int]


@pytest.fixture
def test_cases() -> list[KnightAttackTestCase]:
    return [
        KnightAttackTestCase(
            func_args=(8, 1, 1, 2, 2),
            expected=2,
        ),
        KnightAttackTestCase(
            func_args=(8, 1, 1, 2, 3),
            expected=1,
        ),
        KnightAttackTestCase(
            func_args=(8, 0, 3, 4, 2),
            expected=3,
        ),
        KnightAttackTestCase(
            func_args=(8, 0, 3, 5, 2),
            expected=4,
        ),
        KnightAttackTestCase(
            func_args=(24, 4, 7, 19, 20),
            expected=10,
        ),
        KnightAttackTestCase(
            func_args=(100, 21, 10, 0, 0),
            expected=11,
        ),
        KnightAttackTestCase(
            func_args=(3, 0, 0, 1, 2),
            expected=1,
        ),
        KnightAttackTestCase(
            func_args=(3, 0, 0, 1, 1),
            expected=None,
        ),
    ]


def test_knight_attack(test_cases) -> None:
    for t in test_cases:
        assert knight_attack(*t.func_args) == t.expected
