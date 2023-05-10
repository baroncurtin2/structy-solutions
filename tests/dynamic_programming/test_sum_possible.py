from dataclasses import dataclass

import pytest

from structy.dynamic_programming.sum_possible import sum_possible


@dataclass(slots=True)
class SumPossibleTestCase:
    amount: int
    numbers: list[int]
    expected: bool


@pytest.fixture
def test_cases() -> list[SumPossibleTestCase]:
    return [
        SumPossibleTestCase(
            amount=8,
            numbers=[5, 12, 4],
            expected=True,
        ),
        SumPossibleTestCase(
            amount=15,
            numbers=[6, 2, 10, 19],
            expected=False,
        ),
        SumPossibleTestCase(
            amount=13,
            numbers=[6, 2, 1],
            expected=True,
        ),
        SumPossibleTestCase(
            amount=103,
            numbers=[6, 20, 1],
            expected=True,
        ),
        SumPossibleTestCase(
            amount=12,
            numbers=[],
            expected=False,
        ),
        SumPossibleTestCase(
            amount=12,
            numbers=[12],
            expected=True,
        ),
        SumPossibleTestCase(
            amount=0,
            numbers=[],
            expected=True,
        ),
        SumPossibleTestCase(
            amount=271,
            numbers=[10, 8, 265, 24],
            expected=False,
        ),
        SumPossibleTestCase(
            amount=2017,
            numbers=[4, 2, 10],
            expected=False,
        ),
        SumPossibleTestCase(
            amount=13,
            numbers=[3, 5],
            expected=True,
        ),
    ]


def test_sum_possible(test_cases):
    for t in test_cases:
        assert sum_possible(t.amount, t.numbers) == t.expected
