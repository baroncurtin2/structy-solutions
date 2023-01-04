from dataclasses import dataclass

import pytest

from structy.exhaustive_recursion.permutations import create_combinations, permutations_with_tail_call_optimization


@dataclass(slots=True)
class PermutationsTestCase:
    items: list[str | int]
    expected: list[list[str | int]]


@pytest.fixture
def test_cases() -> list[PermutationsTestCase]:
    return [
        PermutationsTestCase(
            items=["a", "b", "c"],
            expected=[
                ["a", "b", "c"],
                ["b", "a", "c"],
                ["b", "c", "a"],
                ["a", "c", "b"],
                ["c", "a", "b"],
                ["c", "b", "a"],
            ],
        ),
        PermutationsTestCase(
            items=["red", "blue"],
            expected=[
                ["red", "blue"],
                ["blue", "red"],
            ],
        ),
        PermutationsTestCase(
            items=[8, 2, 1, 4],
            expected=[
                [8, 2, 1, 4],
                [2, 8, 1, 4],
                [2, 1, 8, 4],
                [2, 1, 4, 8],
                [8, 1, 2, 4],
                [1, 8, 2, 4],
                [1, 2, 8, 4],
                [1, 2, 4, 8],
                [8, 1, 4, 2],
                [1, 8, 4, 2],
                [1, 4, 8, 2],
                [1, 4, 2, 8],
                [8, 2, 4, 1],
                [2, 8, 4, 1],
                [2, 4, 8, 1],
                [2, 4, 1, 8],
                [8, 4, 2, 1],
                [4, 8, 2, 1],
                [4, 2, 8, 1],
                [4, 2, 1, 8],
                [8, 4, 1, 2],
                [4, 8, 1, 2],
                [4, 1, 8, 2],
                [4, 1, 2, 8],
            ],
        ),
        PermutationsTestCase(
            items=[],
            expected=[[]],
        ),
    ]


def test_permutations(test_cases: list[PermutationsTestCase]) -> None:
    for t in test_cases:
        assert create_combinations(t.items) == t.expected
