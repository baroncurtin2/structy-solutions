from dataclasses import dataclass

import pytest

from structy.mixed_recall.lefty_nodes import (
    BinaryTreeNode,
    NodeValue,
    lefty_nodes_recur,
    lefty_nodes_iter,
)


def case1() -> BinaryTreeNode:
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


def case2() -> BinaryTreeNode:
    u = BinaryTreeNode("u")
    t = BinaryTreeNode("t")
    s = BinaryTreeNode("s")
    r = BinaryTreeNode("r")
    q = BinaryTreeNode("q")
    p = BinaryTreeNode("p")

    u.left = t
    u.right = s
    s.right = r
    r.left = q
    r.right = p
    return u


def case3() -> BinaryTreeNode:
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


def case4() -> BinaryTreeNode:
    n = BinaryTreeNode("n")
    y = BinaryTreeNode("y")
    c = BinaryTreeNode("c")

    n.left = y
    n.right = c
    return n


def case5() -> BinaryTreeNode:
    i = BinaryTreeNode("i")
    n = BinaryTreeNode("n")
    s = BinaryTreeNode("s")
    t = BinaryTreeNode("t")

    i.right = n
    n.left = s
    n.right = t
    return i


def case6():
    return None


@dataclass(slots=True)
class LeftyNodesTestCase:
    root: BinaryTreeNode | None
    expected: list[NodeValue]


@pytest.fixture
def test_cases() -> list[LeftyNodesTestCase]:
    return [
        LeftyNodesTestCase(
            root=case1(),
            expected=["a", "b", "d", "g"],
        ),
        LeftyNodesTestCase(
            root=case2(),
            expected=["u", "t", "r", "q"],
        ),
        LeftyNodesTestCase(
            root=case3(),
            expected=["l", "m", "o", "q"],
        ),
        LeftyNodesTestCase(
            root=case4(),
            expected=["n", "y"],
        ),
        LeftyNodesTestCase(
            root=case5(),
            expected=["i", "n", "s"],
        ),
        LeftyNodesTestCase(
            root=case6(),
            expected=[],
        ),
    ]


def test_lefty_nodes_recur(test_cases) -> None:
    for t in test_cases:
        assert lefty_nodes_recur(t.tree_a) == t.expected


def test_lefty_nodes_iter(test_cases) -> None:
    for t in test_cases:
        assert lefty_nodes_iter(t.tree_a) == t.expected
