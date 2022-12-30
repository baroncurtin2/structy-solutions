from dataclasses import dataclass

import pytest

from structy.stack.decompress_braces import decompress_braces


@dataclass(slots=True)
class DecompressBracesTestCase:
    string: str
    expected: str


@pytest.fixture
def test_cases() -> list[DecompressBracesTestCase]:
    return [
        DecompressBracesTestCase(
            string="2{q}3{tu}v",
            expected="qqtututuv",
        ),
        DecompressBracesTestCase(
            string="ch3{ao}",
            expected="chaoaoao",
        ),
        DecompressBracesTestCase(
            string="2{y3{o}}s",
            expected="yoooyooos",
        ),
        DecompressBracesTestCase(
            string="z3{a2{xy}b}",
            expected="zaxyxybaxyxybaxyxyb",
        ),
        DecompressBracesTestCase(
            string="2{3{r4{e}r}io}",
            expected="reeeerreeeerreeeerioreeeerreeeerreeeerio",
        ),
        DecompressBracesTestCase(
            string="go3{spinn2{ing}s}",
            expected="gospinningingsspinningingsspinningings",
        ),
        DecompressBracesTestCase(
            string="2{l2{if}azu}l",
            expected="lififazulififazul",
        ),
        DecompressBracesTestCase(
            string="3{al4{ec}2{icia}}",
            expected="alececececiciaiciaalececececiciaiciaalececececiciaicia",
        ),
    ]


def test_decompress_braces(test_cases: list[DecompressBracesTestCase]) -> None:
    for t in test_cases:
        assert decompress_braces(t.string) == t.expected
