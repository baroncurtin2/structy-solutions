from dataclasses import dataclass

import pytest

from structy.mixed_recall.binary_search import binary_search


@dataclass(slots=True)
class BinarySearchTestCase:
    numbers: list[int]
    target: int
    expected: int


@pytest.fixture
def test_cases() -> list[BinarySearchTestCase]:
    return [
        BinarySearchTestCase(
            numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            target=6,
            expected=6,
        ),
        BinarySearchTestCase(
            numbers=[0, 6, 8, 12, 16, 19, 20, 24, 28],
            target=27,
            expected=-1,
        ),
        BinarySearchTestCase(
            numbers=[0, 6, 8, 12, 16, 19, 20, 28],
            target=8,
            expected=2,
        ),
        BinarySearchTestCase(
            numbers=[0, 6, 8, 12, 16, 19, 20, 24, 28],
            target=28,
            expected=8,
        ),
        BinarySearchTestCase(
            numbers=[7, 9],
            target=7,
            expected=0,
        ),
        BinarySearchTestCase(
            numbers=[7, 9],
            target=9,
            expected=1,
        ),
        BinarySearchTestCase(
            numbers=[7, 9],
            target=12,
            expected=-1,
        ),
        BinarySearchTestCase(
            numbers=[7],
            target=7,
            expected=0,
        ),
        BinarySearchTestCase(
            numbers=[],
            target=7,
            expected=-1,
        ),
    ]


def test_binary_search(test_cases: list[BinarySearchTestCase]) -> None:
    for tc in test_cases:
        assert binary_search(tc.numbers, tc.target) == tc.expected
