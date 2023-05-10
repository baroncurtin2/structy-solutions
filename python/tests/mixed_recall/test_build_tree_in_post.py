from dataclasses import dataclass

import pytest

from structy.mixed_recall.build_tree_in_post import build_tree_in_post
from structy.mixed_recall.common import BinaryTreeNode


@dataclass(slots=True)
class BuildTreeInPostTestCase:
    in_order: list[str]
    post_order: list[str]
    expected: str


@pytest.fixture
def test_cases() -> list[BuildTreeInPostTestCase]:
    return [
        BuildTreeInPostTestCase(
            in_order=["y", "x", "z"],
            post_order=["y", "z", "x"],
            expected="x",
        ),
        BuildTreeInPostTestCase(
            in_order=["d", "b", "e", "a", "f", "c", "g"],
            post_order=["d", "e", "b", "f", "g", "c", "a"],
            expected="a",
        ),
        BuildTreeInPostTestCase(
            in_order=["d", "b", "g", "e", "h", "a", "c", "f"],
            post_order=["d", "g", "h", "e", "b", "f", "c", "a"],
            expected="a",
        ),
        BuildTreeInPostTestCase(
            in_order=["m", "n"],
            post_order=["m", "n"],
            expected="n",
        ),
        BuildTreeInPostTestCase(
            in_order=["n", "m"],
            post_order=["m", "n"],
            expected="x",
        ),
    ]

def test_build_tree_in_post(test_cases: list[BuildTreeInPostTestCase]) -> None:
    for tc in test_cases:
        assert build_tree_in_post(tc.in_order, tc.post_order).val == tc.expected