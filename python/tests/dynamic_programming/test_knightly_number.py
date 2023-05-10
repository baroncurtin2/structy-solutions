from dataclasses import dataclass

import pytest

from structy.dynamic_programming.knightly_number import knightly_number


@dataclass(slots=True)
class KnightlyNumberTestCase:
    n: int
    m: int
    kr: int
    kc: int
    pr: int
    pc: int
    expected: int


@pytest.fixture
def test_cases() -> list[KnightlyNumberTestCase]:
    return [
        KnightlyNumberTestCase(8, 2, 4, 4, 5, 5, 2),
        KnightlyNumberTestCase(8, 2, 7, 1, 7, 1, 3),
        KnightlyNumberTestCase(8, 2, 5, 4, 5, 4, 8),
        KnightlyNumberTestCase(8, 3, 5, 2, 4, 4, 21),
        KnightlyNumberTestCase(20, 6, 18, 7, 10, 15, 60),
        KnightlyNumberTestCase(20, 12, 8, 3, 9, 14, 98410127),
        KnightlyNumberTestCase(8, 2, 0, 0, 1, 1, 0),
    ]


def test_knightly_number(test_cases: list[KnightlyNumberTestCase]) -> None:
    for t in test_cases:
        assert knightly_number(t.n, t.m, t.kr, t.kc, t.pr, t.pc) == t.expected
