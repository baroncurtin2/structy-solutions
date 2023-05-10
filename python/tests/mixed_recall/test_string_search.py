from dataclasses import dataclass

import pytest

from structy.mixed_recall.string_search import string_search


@dataclass(slots=True)
class StringSearchTestCase:
    grid: list[list[str]]
    s: str
    expected: bool


@pytest.fixture
def test_cases() -> list[StringSearchTestCase]:
    return [
        StringSearchTestCase(
            grid=[
                ["e", "y", "h", "i", "j"],
                ["q", "x", "e", "r", "p"],
                ["r", "o", "l", "l", "n"],
                ["p", "r", "x", "o", "h"],
                ["a", "a", "m", "c", "m"],
            ],
            s="hello",
            expected=True,
        ),
        StringSearchTestCase(
            grid=[
                ["e", "y", "h", "i", "j"],
                ["q", "x", "e", "r", "p"],
                ["r", "o", "l", "l", "n"],
                ["p", "r", "x", "o", "h"],
                ["a", "a", "m", "c", "m"],
            ],
            s="proxy",
            expected=True,
        ),
        StringSearchTestCase(
            grid=[
                ["e", "y", "h", "i", "j"],
                ["q", "x", "e", "r", "p"],
                ["r", "o", "l", "l", "n"],
                ["p", "r", "x", "o", "h"],
                ["a", "a", "m", "c", "m"],
            ],
            s="rolling",
            expected=False,
        ),
        StringSearchTestCase(
            grid=[
                ["e", "y", "h", "i", "j"],
                ["q", "x", "e", "r", "p"],
                ["r", "o", "l", "l", "n"],
                ["p", "r", "x", "o", "h"],
                ["a", "a", "m", "z", "m"],
            ],
            s="zoo",
            expected=False,
        ),
        StringSearchTestCase(
            grid=[
                ["q", "w", "h", "i", "j"],
                ["q", "e", "r", "o", "p"],
                ["h", "y", "t", "x", "z"],
                ["k", "o", "m", "o", "p"],
            ],
            s="qwerty",
            expected=True,
        ),
        StringSearchTestCase(
            grid=[
                ["f", "d", "i", "e", "l", "u", "j", "t", "q", "v", "o", "p"],
                ["o", "p", "b", "e", "m", "w", "m", "l", "h", "j", "s", "v"],
                ["g", "b", "s", "m", "i", "w", "w", "h", "l", "m", "l", "n"],
                ["a", "l", "s", "k", "p", "c", "t", "u", "v", "b", "c", "m"],
                ["m", "t", "c", "k", "e", "n", "r", "b", "a", "z", "l", "c"],
                ["q", "m", "a", "p", "a", "p", "i", "i", "u", "t", "z", "z"],
                ["d", "u", "z", "o", "e", "r", "a", "t", "t", "c", "q", "k"],
                ["f", "u", "z", "g", "c", "i", "k", "v", "o", "f", "s", "w"],
                ["p", "h", "u", "i", "k", "c", "v", "v", "h", "q", "v", "i"],
                ["l", "q", "w", "f", "y", "g", "w", "f", "a", "u", "x", "q"],
            ],
            s="paprika",
            expected=True,
        ),
        StringSearchTestCase(
            grid=[
                ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s"],
                ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s"],
                ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s"],
                ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s"],
                ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s"],
                ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s"],
                ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s"],
                ["s", "s", "s", "s", "s", "s", "s", "s", "s", "x", "x"],
                ["s", "s", "s", "s", "s", "s", "s", "s", "s", "x", "h"],
            ],
            s="ssssssssssh",
            expected=False,
        ),
        StringSearchTestCase(
            grid=[
                ["a", "b", "a"],
                ["t", "x", "x"],
                ["x", "x", "x"],
            ],
            s="abat",
            expected=True,
        ),
    ]


def test_string_search(test_cases: list[StringSearchTestCase]) -> None:
    for tc in test_cases:
        assert string_search(tc.grid, tc.s, True) == tc.expected
        assert string_search(tc.grid, tc.s) == tc.expected
