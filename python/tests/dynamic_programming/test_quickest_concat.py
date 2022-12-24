from dataclasses import dataclass

import pytest

from structy.dynamic_programming.quickest_concat import quickest_concat


@dataclass(slots=True)
class QuickestConcatTestCase:
    s: str
    words: list[str]
    expected: int


@pytest.fixture
def test_cases() -> list[QuickestConcatTestCase]:
    return [
        QuickestConcatTestCase(
            s="caution",
            words=["ca", "ion", "caut", "ut"],
            expected=2,
        ),
        QuickestConcatTestCase(
            s="caution",
            words=["ion", "caut", "caution"],
            expected=1,
        ),
        QuickestConcatTestCase(
            s="respondorreact",
            words=["re", "or", "spond", "act", "respond"],
            expected=4,
        ),
        QuickestConcatTestCase(
            s="simchacindy",
            words=["sim", "simcha", "acindy", "ch"],
            expected=3,
        ),
        QuickestConcatTestCase(
            s="simchacindy",
            words=["sim", "simcha", "acindy"],
            expected=-1,
        ),
        QuickestConcatTestCase(
            s="uuuuuu",
            words=["u", "uu", "uuu", "uuuu"],
            expected=2,
        ),
        QuickestConcatTestCase(
            s="rongbetty",
            words=["wrong", "bet"],
            expected=-1,
        ),
        QuickestConcatTestCase(
            s="uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu",
            words=["u", "uu", "uuu", "uuuu", "uuuuu"],
            expected=7,
        ),
    ]


def test_quickest_concat(test_cases: list[QuickestConcatTestCase]):
    for t in test_cases:
        assert quickest_concat(t.s, t.words) == t.expected
