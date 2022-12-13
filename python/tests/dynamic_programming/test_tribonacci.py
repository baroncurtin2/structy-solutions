import pytest
from dataclasses import dataclass

from structy.dynamic_programming.tribonacci import tribonacci


@dataclass(slots=True)
class TribonacciTestCase:
    n: int
    expected: int


@pytest.fixture
def test_cases() -> list[TribonacciTestCase]:
    return [
        TribonacciTestCase(
            n=0,
            expected=0,
        ),
        TribonacciTestCase(
            n=1,
            expected=0,
        ),
        TribonacciTestCase(
            n=2,
            expected=1,
        ),
        TribonacciTestCase(
            n=5,
            expected=4,
        ),
        TribonacciTestCase(
            n=7,
            expected=13,
        ),
        TribonacciTestCase(
            n=14,
            expected=927,
        ),
        TribonacciTestCase(
            n=20,
            expected=35890,
        ),
        TribonacciTestCase(
            n=37,
            expected=1132436852,
        ),
    ]


def test_tribonacci(test_cases):
    for t in test_cases:
        assert tribonacci(t.n) == t.expected
