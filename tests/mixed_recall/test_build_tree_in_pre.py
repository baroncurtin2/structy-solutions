from dataclasses import dataclass

import pytest

from structy.mixed_recall.build_tree_in_pre import build_tree_in_pre


@dataclass(slots=True)
class BuildTreeInPreTestCase:
    in_order: list[str]
    pre_order: list[str]
    expected: str


@pytest.fixture
def test_cases() -> list[BuildTreeInPreTestCase]:
    return [
        BuildTreeInPreTestCase(
            in_order=["z", "y", "x"],
            pre_order=["y", "z", "x"],
            expected="y",
        ),
        BuildTreeInPreTestCase(
            in_order=["y", "z", "x"],
            pre_order=["y", "x", "z"],
            expected="y",
        ),
        BuildTreeInPreTestCase(
            in_order=["d", "b", "g", "e", "h", "a", "c", "f"],
            pre_order=["a", "b", "d", "e", "g", "h", "c", "f"],
            expected="a",
        ),
        BuildTreeInPreTestCase(
            in_order=["t", "u", "s", "q", "r", "p"],
            pre_order=["u", "t", "s", "r", "q", "p"],
            expected="u",
        ),
        BuildTreeInPreTestCase(
            in_order=["m", "l", "q", "o", "r", "n", "s", "p", "t"],
            pre_order=["l", "m", "n", "o", "q", "r", "p", "s", "t"],
            expected="l",
        ),
    ]


def test_build_tree_in_pre(test_cases: list[BuildTreeInPreTestCase]) -> None:
    for tc in test_cases:
        assert build_tree_in_pre(tc.in_order, tc.pre_order).val == tc.expected
