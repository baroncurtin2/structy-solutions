from dataclasses import dataclass

import pytest

from structy.dynamic_programming.summing_squares import summing_squares


@dataclass(slots=True)
class SummingSquaresTestCase:
    n: int
    expected: int


@pytest.fixture
def test_cases() -> list[SummingSquaresTestCase]:
    return [
        SummingSquaresTestCase(n=8, expected=2),
        SummingSquaresTestCase(n=9, expected=1),
        SummingSquaresTestCase(n=12, expected=3),
        SummingSquaresTestCase(n=1, expected=1),
        SummingSquaresTestCase(n=31, expected=4),
        SummingSquaresTestCase(n=50, expected=2),
        SummingSquaresTestCase(n=68, expected=2),
        SummingSquaresTestCase(n=87, expected=4),
    ]


def test_summing_squares(test_cases):
    for t in test_cases:
        assert summing_squares(t.n) == t.expected
