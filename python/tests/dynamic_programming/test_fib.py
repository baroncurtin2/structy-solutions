from dataclasses import dataclass
import pytest

from structy.dynamic_programming.fib import fib


@dataclass(slots=True)
class FibTestCase:
    n: int
    expected: int


@pytest.fixture
def test_cases() -> list[FibTestCase]:
    return [
        FibTestCase(
            n=0,
            expected=0,
        ),
        FibTestCase(
            n=1,
            expected=1,
        ),
        FibTestCase(
            n=2,
            expected=1,
        ),
        FibTestCase(
            n=3,
            expected=2,
        ),
        FibTestCase(
            n=4,
            expected=3,
        ),
        FibTestCase(
            n=5,
            expected=5,
        ),
        FibTestCase(
            n=35,
            expected=9227465,
        ),
        FibTestCase(
            n=46,
            expected=1836311903,
        ),
    ]


def test_fib(test_cases) -> None:
    for t in test_cases:
        assert fib(t.n) == t.expected
