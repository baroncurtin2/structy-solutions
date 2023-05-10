from dataclasses import dataclass

import pytest

from structy.mixed_recall.lexical_order import lexical_order


@dataclass(slots=True)
class LexicalOrderTestCase:
    word_1: str
    word_2: str
    alphabet: str
    expected: bool


@pytest.fixture
def test_cases() -> list[LexicalOrderTestCase]:
    alphabet_1 = "abcdefghijklmnopqrstuvwxyz"
    alphabet_2 = "ghzstijbacdopnfklmeqrxyuvw"

    return [
        LexicalOrderTestCase(
            word_1="apple",
            word_2="dock",
            alphabet=alphabet_1,
            expected=True,
        ),
        LexicalOrderTestCase(
            word_1="apple",
            word_2="ample",
            alphabet=alphabet_1,
            expected=False,
        ),
        LexicalOrderTestCase(
            word_1="app",
            word_2="application",
            alphabet=alphabet_1,
            expected=True,
        ),
        LexicalOrderTestCase(
            word_1="backs",
            word_2="backdoor",
            alphabet=alphabet_1,
            expected=False,
        ),
        LexicalOrderTestCase(
            word_1="zoo",
            word_2="dinner",
            alphabet=alphabet_2,
            expected=True,
        ),
        LexicalOrderTestCase(
            word_1="leaper",
            word_2="leap",
            alphabet=alphabet_2,
            expected=False,
        ),
        LexicalOrderTestCase(
            word_1="backs",
            word_2="backdoor",
            alphabet=alphabet_2,
            expected=True,
        ),
        LexicalOrderTestCase(
            word_1="semper",
            word_2="semper",
            alphabet=alphabet_2,
            expected=True,
        ),
    ]


def test_lexical_order(test_cases: list[LexicalOrderTestCase]) -> None:
    for tc in test_cases:
        assert lexical_order(tc.word_1, tc.word_2, tc.alphabet) == tc.expected


