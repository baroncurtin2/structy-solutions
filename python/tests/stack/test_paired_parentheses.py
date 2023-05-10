from dataclasses import dataclass

import pytest

from structy.stack.paired_parentheses import paired_parentheses


@dataclass(slots=True)
class PairedParenthesesTestCase:
    string: str
    expected: bool


@pytest.fixture
def test_cases() -> list[PairedParenthesesTestCase]:
    return [
        PairedParenthesesTestCase(
            string="(david)((abby))",
            expected=True,
        ),
        PairedParenthesesTestCase(
            string="()rose(jeff",
            expected=False,
        ),
        PairedParenthesesTestCase(
            string=")(",
            expected=False,
        ),
        PairedParenthesesTestCase(
            string="()",
            expected=True,
        ),
        PairedParenthesesTestCase(
            string="(((potato())))",
            expected=True,
        ),
        PairedParenthesesTestCase(
            string="(())(water)()",
            expected=True,
        ),
        PairedParenthesesTestCase(
            string="(())(water()()",
            expected=False,
        ),
        PairedParenthesesTestCase(
            string="",
            expected=True,
        ),
        PairedParenthesesTestCase(
            string="))()",
            expected=False,
        ),
    ]


def test_paired_parentheses(test_cases: list[PairedParenthesesTestCase]) -> None:
    for t in test_cases:
        assert paired_parentheses(t.string) == t.expected
