from dataclasses import dataclass

import pytest

from structy.dynamic_programming.min_change import min_change


@dataclass(slots=True)
class MinChangeTestCase:
    amount: int
    coins: list[int]
    expected: int


@pytest.fixture
def test_cases() -> list[MinChangeTestCase]:
    return [
        MinChangeTestCase(
            amount=8,
            coins=[1, 5, 4, 12],
            expected=2,
        ),
        MinChangeTestCase(
            amount=13,
            coins=[1, 9, 5, 14, 30],
            expected=5,
        ),
        MinChangeTestCase(
            amount=23,
            coins=[2, 5, 7],
            expected=4,
        ),
        MinChangeTestCase(
            amount=102,
            coins=[1, 5, 10, 25],
            expected=6,
        ),
        MinChangeTestCase(
            amount=200,
            coins=[1, 5, 10, 25],
            expected=8,
        ),
        MinChangeTestCase(
            amount=2017,
            coins=[4, 2, 10],
            expected=-1,
        ),
        MinChangeTestCase(
            amount=271,
            coins=[10, 8, 265, 24],
            expected=-1,
        ),
        MinChangeTestCase(
            amount=0,
            coins=[4, 2, 10],
            expected=0,
        ),
        MinChangeTestCase(
            amount=0,
            coins=[],
            expected=0,
        ),
    ]


def test_min_change(test_cases):
    for t in test_cases:
        assert min_change(t.amount, t.coins) == t.expected
