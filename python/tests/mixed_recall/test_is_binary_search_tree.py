from dataclasses import dataclass

import pytest

from structy.mixed_recall.common import BinaryTreeNode
from structy.mixed_recall.is_binary_search_tree import is_binary_search_tree


@dataclass(slots=True)
class IsBinarySearchTreeTestCase:
    root: BinaryTreeNode
    expected: bool


def tree_0() -> BinaryTreeNode:
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


def tree_1() -> BinaryTreeNode:
    a = BinaryTreeNode(12)
    b = BinaryTreeNode(5)
    c = BinaryTreeNode(18)
    d = BinaryTreeNode(3)
    e = BinaryTreeNode(15)
    f = BinaryTreeNode(19)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    return a


def tree_2() -> BinaryTreeNode:
    a = BinaryTreeNode(12)
    b = BinaryTreeNode(5)
    c = BinaryTreeNode(19)
    d = BinaryTreeNode(3)
    e = BinaryTreeNode(9)
    f = BinaryTreeNode(19)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    return a


def tree_3() -> BinaryTreeNode:
    a = BinaryTreeNode(12)
    b = BinaryTreeNode(5)
    c = BinaryTreeNode(10)
    d = BinaryTreeNode(3)
    e = BinaryTreeNode(9)
    f = BinaryTreeNode(19)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    return a


def tree_4() -> BinaryTreeNode:
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
def test_cases() -> list[IsBinarySearchTreeTestCase]:
    return [
        IsBinarySearchTreeTestCase(
            root=tree_0(),
            expected=True,
        ),
        IsBinarySearchTreeTestCase(
            root=tree_1(),
            expected=False,
        ),
        IsBinarySearchTreeTestCase(
            root=tree_2(),
            expected=True,
        ),
        IsBinarySearchTreeTestCase(
            root=tree_3(),
            expected=False,
        ),
        IsBinarySearchTreeTestCase(
            root=tree_4(),
            expected=True,
        ),
    ]


def test_is_binary_search_tree(test_cases: list[IsBinarySearchTreeTestCase]) -> None:
    for tc in test_cases:
        assert is_binary_search_tree(tc.root, False) == tc.expected
        assert is_binary_search_tree(tc.root, True) == tc.expected
