from dataclasses import dataclass

import pytest

from structy.mixed_recall.token_replace import token_replace


@dataclass(slots=True)
class TokenReplaceTestCase:
    s: str
    tokens: dict[str, str]
    expected: str


@pytest.fixture
def test_cases() -> list[TokenReplaceTestCase]:
    return [
        TokenReplaceTestCase(
            s="Walk the $ANIMAL$ in the $LOCATION$!",
            tokens={
                "$LOCATION$": "park",
                "$ANIMAL$": "dog",
            },
            expected="Walk the dog in the park!",
        ),
        TokenReplaceTestCase(
            s="the $ADJECTIVE$ fox $VERB$ $ADJECTIVE$ly $DIRECTION$ward",
            tokens={"$ADJECTIVE$": "quick", "$VERB$": "hopped", "$DIRECTION$": "North"},
            expected="the quick fox hopped quickly Northward",
        ),
        TokenReplaceTestCase(
            s="his greeting is always $greeting$.",
            tokens={
                "$greeting$": "hey programmer",
            },
            expected="his greeting is always hey programmer.",
        ),
        TokenReplaceTestCase(
            s="$A$$B$$C$, oh my.",
            tokens={
                "$A$": "lions",
                "$B$": "tigers",
                "$C$": "bears",
            },
            expected="lionstigersbears, oh my.",
        ),
        TokenReplaceTestCase(
            s="$B$",
            tokens={
                "$A$": "lions",
                "$B$": "tigers",
                "$C$": "bears",
            },
            expected="tigers",
        ),
        TokenReplaceTestCase(
            s="$first$second$third$",
            tokens={
                "$second$": "beta",
                "$first$": "alpha",
                "$third$": "gamma",
            },
            expected="alphasecondgamma",
        ),
    ]


def test_token_replace(test_cases: list[TokenReplaceTestCase]) -> None:
    for tc in test_cases:
        assert token_replace(tc.s, tc.tokens) == tc.expected
