from dataclasses import dataclass

import pytest

from structy.mixed_recall.common import BinaryTreeNode, BinaryTree, NodeValue
from structy.mixed_recall.lowest_common_ancestor import lowest_common_ancestor


def tree1() -> BinaryTree:
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

    tree = BinaryTree()
    tree.root = a
    return tree


def tree2() -> BinaryTree:
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

    tree = BinaryTree()
    tree.root = l
    return tree


@dataclass(slots=True)
class LowestCommonAncestorTestCase:
    tree: BinaryTree
    val1: NodeValue
    val2: NodeValue
    expected: NodeValue


@pytest.fixture
def test_cases1() -> list[LowestCommonAncestorTestCase]:
    return [
        LowestCommonAncestorTestCase(
            tree=tree1(),
            val1="d",
            val2="h",
            expected="b",
        ),
        LowestCommonAncestorTestCase(
            tree=tree1(),
            val1="d",
            val2="g",
            expected="b",
        ),
        LowestCommonAncestorTestCase(
            tree=tree1(),
            val1="g",
            val2="c",
            expected="a",
        ),
        LowestCommonAncestorTestCase(
            tree=tree1(),
            val1="b",
            val2="g",
            expected="b",
        ),
        LowestCommonAncestorTestCase(
            tree=tree1(),
            val1="f",
            val2="c",
            expected="c",
        ),
    ]


@pytest.fixture
def test_cases2() -> list[LowestCommonAncestorTestCase]:
    return [
        LowestCommonAncestorTestCase(
            tree=tree2(),
            val1="r",
            val2="p",
            expected="n",
        ),
        LowestCommonAncestorTestCase(
            tree=tree2(),
            val1="m",
            val2="o",
            expected="l",
        ),
        LowestCommonAncestorTestCase(
            tree=tree2(),
            val1="t",
            val2="q",
            expected="n",
        ),
        LowestCommonAncestorTestCase(
            tree=tree2(),
            val1="s",
            val2="p",
            expected="p",
        ),
    ]


def test_lowest_common_ancestor(
    test_cases1: list[LowestCommonAncestorTestCase], test_cases2: list[LowestCommonAncestorTestCase]
) -> None:
    for t1 in test_cases1:
        assert lowest_common_ancestor(t1.tree.root, t1.val1, t1.val2) == t1.expected

    for t2 in test_cases2:
        assert lowest_common_ancestor(t2.tree.root, t2.val1, t2.val2) == t2.expected
