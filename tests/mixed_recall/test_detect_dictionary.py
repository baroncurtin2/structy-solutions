from dataclasses import dataclass

import pytest

from structy.mixed_recall.detect_dictionary import detect_dictionary


@dataclass(slots=True)
class DetectDictionaryTestCase:
    dictionary: list[str]
    alphabet: str
    expected: bool


@pytest.fixture
def test_cases() -> list[DetectDictionaryTestCase]:
    return [
        DetectDictionaryTestCase(
            dictionary=["zoo", "tick", "tack", "door"],
            alphabet="ghzstijbacdopnfklmeqrxyuvw",
            expected=True,
        ),
        DetectDictionaryTestCase(
            dictionary=["zoo", "tack", "tick", "door"],
            alphabet="ghzstijbacdopnfklmeqrxyuvw",
            expected=False,
        ),
        DetectDictionaryTestCase(
            dictionary=["zoos", "zoo", "tick", "tack", "door"],
            alphabet="ghzstijbacdopnfklmeqrxyuvw",
            expected=False,
        ),
        DetectDictionaryTestCase(
            dictionary=["miles", "milestone", "proper", "process", "goal"],
            alphabet="mnoijpqrshkltabcdefguvwzxy",
            expected=True,
        ),
        DetectDictionaryTestCase(
            dictionary=["miles", "milestone", "pint", "proper", "process", "goal"],
            alphabet="mnoijpqrshkltabcdefguvwzxy",
            expected=True,
        ),
        DetectDictionaryTestCase(
            dictionary=["miles", "milestone", "pint", "proper", "process", "goal", "apple"],
            alphabet="mnoijpqrshkltabcdefguvwzxy",
            expected=False,
        ),
    ]


def test_detect_dictionary(test_cases: list[DetectDictionaryTestCase]) -> None:
    for tc in test_cases:
        assert detect_dictionary(tc.dictionary, tc.alphabet) == tc.expected
