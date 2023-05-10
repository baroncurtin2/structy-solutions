from dataclasses import dataclass

import pytest

from structy.exhaustive_recursion.parenthetical_possibilities import parenthetical_possibilities


@dataclass(slots=True)
class ParentheticalPossibilitiesTestCase:
    s: str
    expected: list[str]


@pytest.fixture
def test_cases() -> list[ParentheticalPossibilitiesTestCase]:
    return [
        ParentheticalPossibilitiesTestCase(
            s="x(mn)yz",
            expected=["xmyz", "xnyz"],
        ),
        ParentheticalPossibilitiesTestCase(
            s="(qr)ab(stu)c",
            expected=[
                "qabsc",
                "qabtc",
                "qabuc",
                "rabsc",
                "rabtc",
                "rabuc",
            ],
        ),
        ParentheticalPossibilitiesTestCase(
            s="taco",
            expected=["taco"],
        ),
        ParentheticalPossibilitiesTestCase(
            s="",
            expected=[""],
        ),
        ParentheticalPossibilitiesTestCase(
            s="(etc)(blvd)(cat)",
            expected=[
                "ebc",
                "eba",
                "ebt",
                "elc",
                "ela",
                "elt",
                "evc",
                "eva",
                "evt",
                "edc",
                "eda",
                "edt",
                "tbc",
                "tba",
                "tbt",
                "tlc",
                "tla",
                "tlt",
                "tvc",
                "tva",
                "tvt",
                "tdc",
                "tda",
                "tdt",
                "cbc",
                "cba",
                "cbt",
                "clc",
                "cla",
                "clt",
                "cvc",
                "cva",
                "cvt",
                "cdc",
                "cda",
                "cdt",
            ],
        ),
    ]


def test_parenthetical_possibilities(test_cases: list[ParentheticalPossibilitiesTestCase]) -> None:
    for t in test_cases:
        assert parenthetical_possibilities(t.s) == t.expected
