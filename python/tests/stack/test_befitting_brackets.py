from dataclasses import dataclass

import pytest

from structy.stack.befitting_brackets import befitting_brackets


@dataclass(slots=True)
class BefittingBracketsTestCase:
    string: str
    expected: bool


@pytest.fixture
def test_cases() -> list[BefittingBracketsTestCase]:
    return [
        BefittingBracketsTestCase(
            string="(){}[](())",
            expected=True,
        ),
        BefittingBracketsTestCase(
            string="({[]})",
            expected=True,
        ),
        BefittingBracketsTestCase(
            string="[][}",
            expected=False,
        ),
        BefittingBracketsTestCase(
            string="{[]}({}",
            expected=False,
        ),
        BefittingBracketsTestCase(
            string="[]{}(}[]",
            expected=False,
        ),
        BefittingBracketsTestCase(
            string="[]{}()[]",
            expected=True,
        ),
        BefittingBracketsTestCase(
            string="]{}",
            expected=False,
        ),
        BefittingBracketsTestCase(
            string="",
            expected=True,
        ),
        BefittingBracketsTestCase(
            string="{[(}])",
            expected=False,
        ),
    ]


def test_befitting_brackets(test_cases: list[BefittingBracketsTestCase]) -> None:
    for t in test_cases:
        assert befitting_brackets(t.string) == t.expected
