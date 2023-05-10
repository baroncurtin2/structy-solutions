from dataclasses import dataclass

import pytest

from structy.dynamic_programming.counting_change import counting_change


@dataclass(slots=True)
class CountingChangeTestCase:
    amount: int
    coins: list[int]
    expected: int


@pytest.fixture
def test_cases() -> list[CountingChangeTestCase]:
    return [
        CountingChangeTestCase(
            amount=4,
            coins=[1, 2, 3],
            expected=4,
        ),
        CountingChangeTestCase(
            amount=8,
            coins=[1, 2, 3],
            expected=10,
        ),
        CountingChangeTestCase(
            amount=24,
            coins=[5, 7, 3],
            expected=5,
        ),
        CountingChangeTestCase(
            amount=13,
            coins=[2, 6, 12, 10],
            expected=0,
        ),
        CountingChangeTestCase(
            amount=512,
            coins=[1, 5, 10, 25],
            expected=20119,
        ),
        CountingChangeTestCase(
            amount=1000,
            coins=[1, 5, 10, 25],
            expected=142_511,
        ),
        CountingChangeTestCase(
            amount=240,
            coins=[1, 2, 3, 4, 5, 6, 7, 8, 9],
            expected=1_525_987_916,
        ),
    ]


def test_counting_change(test_cases):
    for t in test_cases:
        assert counting_change(t.amount, t.coins) == t.expected
