from dataclasses import dataclass

import pytest

from structy.mixed_recall.common import BinaryTreeNode, NodeValue
from structy.mixed_recall.post_order import post_order


@dataclass(slots=True)
class PostOrderTestCase:
    root: BinaryTreeNode
    expected: list[NodeValue]


def tree_0() -> BinaryTreeNode:
    x = BinaryTreeNode("x")
    y = BinaryTreeNode("y")
    z = BinaryTreeNode("z")

    x.left = y
    x.right = z

    return x


def tree_1() -> BinaryTreeNode:
    a = BinaryTreeNode("a")
    b = BinaryTreeNode("b")
    c = BinaryTreeNode("c")
    d = BinaryTreeNode("d")
    e = BinaryTreeNode("e")
    f = BinaryTreeNode("f")
    g = BinaryTreeNode("g")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    return a


def tree_2() -> BinaryTreeNode:
    a = BinaryTreeNode("a")
    b = BinaryTreeNode("b")
    c = BinaryTreeNode("c")
    d = BinaryTreeNode("d")
    e = BinaryTreeNode("e")
    f = BinaryTreeNode("f")
    g = BinaryTreeNode("g")
    h = BinaryTreeNode("h")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h

    return a


def tree_3() -> BinaryTreeNode:
    l = BinaryTreeNode("l")
    m = BinaryTreeNode("m")
    n = BinaryTreeNode("n")
    o = BinaryTreeNode("o")
    p = BinaryTreeNode("p")
    q = BinaryTreeNode("q")
    r = BinaryTreeNode("r")
    s = BinaryTreeNode("s")
    t = BinaryTreeNode("t")

    l.left = m
    l.right = n
    n.left = o
    n.right = p
    o.left = q
    o.right = r
    p.left = s
    p.right = t

    return l


def tree_4() -> BinaryTreeNode | None:
    return None


@pytest.fixture
def test_cases() -> list[PostOrderTestCase]:
    return [
        PostOrderTestCase(
            root=tree_0(),
            expected=["y", "z", "x"],
        ),
        PostOrderTestCase(
            root=tree_1(),
            expected=["d", "e", "b", "f", "g", "c", "a"],
        ),
        PostOrderTestCase(
            root=tree_2(),
            expected=["d", "g", "h", "e", "b", "f", "c", "a"],
        ),
        PostOrderTestCase(
            root=tree_3(),
            expected=["m", "q", "r", "o", "s", "t", "p", "n", "l"],
        ),
        PostOrderTestCase(
            root=tree_4(),
            expected=[],
        ),
    ]


def test_post_order(test_cases: list[PostOrderTestCase]) -> None:
    for tc in test_cases:
        assert post_order(tc.root, True) == tc.expected
        assert post_order(tc.root, False) == tc.expected
