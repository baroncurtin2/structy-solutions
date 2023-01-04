from dataclasses import dataclass

import pytest

from structy.exhaustive_recursion.create_combinations import create_combinations


@dataclass(slots=True)
class CreateCombinationsTestCase:
    items: list[str | int]
    k: int
    expected: list[list[str | int]]


@pytest.fixture
def test_cases() -> list[CreateCombinationsTestCase]:
    return [
        CreateCombinationsTestCase(
            items=["a", "b", "c"],
            k=2,
            expected=[
                ["a", "b"],
                ["a", "c"],
                ["b", "c"],
            ],
        ),
        CreateCombinationsTestCase(
            items=["q", "r", "s", "t"],
            k=2,
            expected=[
                ["q", "r"],
                ["q", "s"],
                ["q", "t"],
                ["r", "s"],
                ["r", "t"],
                ["s", "t"],
            ],
        ),
        CreateCombinationsTestCase(
            items=["q", "r", "s", "t"],
            k=3,
            expected=[
                ["q", "r", "s"],
                ["q", "r", "t"],
                ["q", "s", "t"],
                ["r", "s", "t"],
            ],
        ),
        CreateCombinationsTestCase(
            items=[1, 28, 94],
            k=3,
            expected=[
                [1, 28, 94],
            ],
        ),
    ]


def test_create_combinations(test_cases: list[CreateCombinationsTestCase]) -> None:
    for t in test_cases:
        assert create_combinations(t.items, t.k) == t.expected
