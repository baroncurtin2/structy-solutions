from dataclasses import dataclass

import pytest

from structy.dynamic_programming.max_palin_subsequence import max_palin_subsequence


@dataclass(slots=True)
class MaxPalinSubsequenceTestCase:
    string: str
    expected: int


@pytest.fixture
def test_cases() -> list[MaxPalinSubsequenceTestCase]:
    return [
        MaxPalinSubsequenceTestCase(
            string="luwxult",
            expected=5,
        ),
        MaxPalinSubsequenceTestCase(
            string="xyzaxxzy",
            expected=6,
        ),
        MaxPalinSubsequenceTestCase(
            string="lol",
            expected=3,
        ),
        MaxPalinSubsequenceTestCase(
            string="boabcdefop",
            expected=3,
        ),
        MaxPalinSubsequenceTestCase(
            string="z",
            expected=1,
        ),
        MaxPalinSubsequenceTestCase(
            string="chartreusepugvicefree",
            expected=7,
        ),
        MaxPalinSubsequenceTestCase(
            string="qwueoiuahsdjnweuueueunasdnmnqweuzqwerty",
            expected=15,
        ),
        MaxPalinSubsequenceTestCase(
            string="enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe",
            expected=31,
        ),
    ]


def test_max_palin_subsequence(test_cases):
    for t in test_cases:
        assert max_palin_subsequence(t.string) == t.expected
