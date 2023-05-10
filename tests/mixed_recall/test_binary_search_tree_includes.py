from dataclasses import dataclass

import pytest

from structy.mixed_recall.binary_search_tree_includes import binary_search_tree_includes
from structy.mixed_recall.common import BinaryTreeNode


@dataclass(slots=True)
class BinarySearchTreeIncludesTestCase:
    root: BinaryTreeNode
    target: int
    expected: bool


def tree_a() -> BinaryTreeNode:
    a = BinaryTreeNode(12)
    b = BinaryTreeNode(5)
    c = BinaryTreeNode(18)
    d = BinaryTreeNode(3)
    e = BinaryTreeNode(9)
    f = BinaryTreeNode(19)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    return a


def tree_b() -> BinaryTreeNode:
    q = BinaryTreeNode(54)
    r = BinaryTreeNode(42)
    s = BinaryTreeNode(70)
    t = BinaryTreeNode(31)
    u = BinaryTreeNode(50)
    v = BinaryTreeNode(72)
    w = BinaryTreeNode(47)
    x = BinaryTreeNode(90)

    q.left = r
    q.right = s
    r.left = t
    r.right = u
    s.right = v
    u.left = w
    v.right = x

    return q


@pytest.fixture
def test_cases() -> list[BinarySearchTreeIncludesTestCase]:
    return [
        BinarySearchTreeIncludesTestCase(
            root=tree_a(),
            target=9,
            expected=True,
        ),
        BinarySearchTreeIncludesTestCase(
            root=tree_a(),
            target=15,
            expected=False,
        ),
        BinarySearchTreeIncludesTestCase(
            root=tree_a(),
            target=1,
            expected=False,
        ),
        BinarySearchTreeIncludesTestCase(
            root=tree_a(),
            target=12,
            expected=True,
        ),
        BinarySearchTreeIncludesTestCase(
            root=tree_b(),
            target=55,
            expected=False,
        ),
        BinarySearchTreeIncludesTestCase(
            root=tree_b(),
            target=47,
            expected=True,
        ),
        BinarySearchTreeIncludesTestCase(
            root=tree_b(),
            target=49,
            expected=False,
        ),
        BinarySearchTreeIncludesTestCase(
            root=tree_b(),
            target=70,
            expected=True,
        ),
        BinarySearchTreeIncludesTestCase(
            root=tree_b(),
            target=100,
            expected=False,
        ),
    ]


def test_binary_search_tree_includes(test_cases: list[BinarySearchTreeIncludesTestCase]) -> None:
    for tc in test_cases:
        assert binary_search_tree_includes(tc.root, tc.target) == tc.expected
