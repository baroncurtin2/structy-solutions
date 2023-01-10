from dataclasses import dataclass

import pytest

from structy.dynamic_programming.can_concat import can_concat


@dataclass(slots=True)
class CanConcatTestCase:
    s: str
    words: list[str]
    expected: bool


@pytest.fixture
def test_cases() -> list[CanConcatTestCase]:
    return [
        CanConcatTestCase(
            s="oneisnone",
            words=["one", "none", "is"],
            expected=True,
        ),
        CanConcatTestCase(
            s="oneisnone",
            words=["on", "e", "is"],
            expected=False,
        ),
        CanConcatTestCase(
            s="oneisnone",
            words=["on", "e", "is", "n"],
            expected=True,
        ),
        CanConcatTestCase(
            s="foodisgood",
            words=["is", "g", "ood", "f"],
            expected=True,
        ),
        CanConcatTestCase(
            s="santahat",
            words=["santah", "hat"],
            expected=False,
        ),
        CanConcatTestCase(
            s="santahat",
            words=["santah", "san", "hat", "tahat"],
            expected=True,
        ),
        CanConcatTestCase(
            s="rrrrrrrrrrrrrrrrrrrrrrrrrrx",
            words=["r", "rr", "rrr", "rrrr", "rrrrr", "rrrrrr"],
            expected=False,
        ),
        CanConcatTestCase(
            s="fooisgood",
            words=["foo", "is", "g", "ood", "f"],
            expected=True,
        ),
    ]


def test_can_concat(test_cases):
    for t in test_cases:
        assert can_concat(t.s, t.words) == t.expected
