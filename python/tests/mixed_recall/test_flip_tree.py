from dataclasses import dataclass

import pytest

from structy.mixed_recall.common import BinaryTreeNode
from structy.mixed_recall.flip_tree import flip_tree, flip_tree_iter


def tree1() -> BinaryTreeNode:
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


def tree2() -> BinaryTreeNode:
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


def tree3() -> BinaryTreeNode:
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


def tree4() -> BinaryTreeNode:
    n = BinaryTreeNode("n")
    y = BinaryTreeNode("y")
    c = BinaryTreeNode("c")

    n.left = y
    n.right = c
    return n


@dataclass(slots=True)
class FlipTreeTestCase:
    root: BinaryTreeNode


@pytest.fixture
def test_cases() -> list[FlipTreeTestCase]:
    return [
        FlipTreeTestCase(root=tree1()),
        FlipTreeTestCase(root=tree2()),
        FlipTreeTestCase(root=tree3()),
        FlipTreeTestCase(root=tree4()),
    ]


def test_flip_tree(test_cases) -> None:
    for t in test_cases:
        root = t.tree_a
        flipped_root = flip_tree(root)

        assert root.val == flipped_root.val
        assert root.left.val == flipped_root.right.val
        assert root.right.val == flipped_root.left.val


def test_flip_tree_iter(test_cases) -> None:
    for t in test_cases:
        root = t.tree_a
        flipped_root = flip_tree_iter(root)

        assert root.val == flipped_root.val
        assert root.left.val == flipped_root.right.val
        assert root.right.val == flipped_root.left.val
