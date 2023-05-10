from dataclasses import dataclass

import pytest

from structy.dynamic_programming.overlap_subsequence import overlap_subsequence


@dataclass(slots=True)
class OverlapSubsequenceTestCase:
    string1: str
    string2: str
    expected: int


@pytest.fixture
def test_cases() -> list[OverlapSubsequenceTestCase]:
    return [
        OverlapSubsequenceTestCase(
            string1="dogs",
            string2="daogt",
            expected=3,
        ),
        OverlapSubsequenceTestCase(
            string1="xcyats",
            string2="criaotsi",
            expected=4,
        ),
        OverlapSubsequenceTestCase(
            string1="xfeqortsver",
            string2="feeeuavoeqr",
            expected=5,
        ),
        OverlapSubsequenceTestCase(
            string1="kinfolklivemustache",
            string2="bespokekinfolksnackwave",
            expected=11,
        ),
        OverlapSubsequenceTestCase(
            string1="mumblecorebeardleggingsauthenticunicorn",
            string2="succulentspughumblemeditationlocavore",
            expected=15,
        ),
    ]


def test_overlap_subsequence(test_cases):
    for t in test_cases:
        assert overlap_subsequence(t.string1, t.string2) == t.expected
