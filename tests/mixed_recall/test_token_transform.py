from dataclasses import dataclass

import pytest

from structy.mixed_recall.token_transform import token_transform


@dataclass(slots=True)
class TokenTransformTestCase:
    s: str
    tokens: dict[str, str]
    expected: str


@pytest.fixture
def test_cases() -> list[TokenTransformTestCase]:
    return [
        TokenTransformTestCase(
            s="Walk the $ANIMAL$ in the $LOCATION$!",
            tokens={
                "$LOCATION$": "$ANIMAL$ park",
                "$ANIMAL$": "dog",
            },
            expected="Walk the dog in the dog park!",
        ),
        TokenTransformTestCase(
            s="the $ADJECTIVE_1$ fox $ADVERBS$ $VERB$ward",
            tokens={
                "$ADJECTIVE_1$": "quick",
                "$ADJECTIVE_2$": "eager",
                "$ADVERBS$": "$ADJECTIVE_1$ly and $ADJECTIVE_2$ly",
                "$VERB$": "hopped $DIRECTION$",
                "$DIRECTION$": "North",
            },
            expected="the quick fox quickly and eagerly hopped Northward",
        ),
        TokenTransformTestCase(
            s="What a $A$ here!",
            tokens={
                "$B$": "epicly $C$",
                "$A$": "pretty $B$ problem $D$",
                "$D$": "we have",
                "$C$": "clever",
            },
            expected="What a pretty epicly clever problem we have here!",
        ),
        TokenTransformTestCase(
            s="$1$ $1$ $1$ $1$ $1$ $1$ $4$ $4$",
            tokens={
                "$1$": "a$2$",
                "$2$": "b$3$",
                "$3$": "c$4$",
                "$4$": "d$5$",
                "$5$": "e$6$",
                "$6$": "f!",
            },
            expected="abcdef! abcdef! abcdef! abcdef! abcdef! abcdef! def! def!",
        ),
        TokenTransformTestCase(
            s="z$0$z$0$z$0$z$0$z$0$z$0$z",
            tokens={
                "$0$": "$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$",
                "$1$": "$2$$2$$2$$2$$2$$2$$2$$2$$2$",
                "$2$": "$3$$3$$3$$3$$3$$3$$3$",
                "$3$": "$4$$4$$4$$4$$4$$4$",
                "$4$": "$5$$5$$5$$5$$5$",
                "$5$": "$6$$6$$6$$6$",
                "$6$": "$7$$7$$7$",
                "$7$": "$8$$8$",
                "$8$": "",
            },
            expected="zzzzzzz",
        ),
    ]


def test_token_transform(test_cases: list[TokenTransformTestCase]) -> None:
    for tc in test_cases:
        assert token_transform(tc.s, tc.tokens) == tc.expected
