from dataclasses import dataclass

import pytest

from structy.stack.nesting_score import nesting_score


@dataclass(slots=True)
class NestingScoreTestCase:
    string: str
    expected: int


@pytest.fixture
def test_cases() -> list[NestingScoreTestCase]:
    return [
        NestingScoreTestCase(
            string="[]",
            expected=1,
        ),
        NestingScoreTestCase(
            string="[][][]",
            expected=3,
        ),
        NestingScoreTestCase(
            string="[[]]",
            expected=2,
        ),
        NestingScoreTestCase(
            string="[[][]]",
            expected=4,
        ),
        NestingScoreTestCase(
            string="[[][][]]",
            expected=6,
        ),
        NestingScoreTestCase(
            string="[[][]][]",
            expected=5,
        ),
        NestingScoreTestCase(
            string="[][[][]][[]]",
            expected=7,
        ),
        NestingScoreTestCase(
            string="[[[[[[[][]]]]]]][]",
            expected=129,
        ),
    ]


def test_nesting_score(test_cases: list[NestingScoreTestCase]) -> None:
    for t in test_cases:
        assert nesting_score(t.string) == t.expected
