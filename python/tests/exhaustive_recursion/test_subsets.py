from dataclasses import dataclass

import pytest

from structy.exhaustive_recursion.subsets import subsets


@dataclass(slots=True)
class SubsetsTestCase:
    elements: list[str]
    expected: list[list[str]]


@pytest.fixture
def test_cases() -> list[SubsetsTestCase]:
    return [
        SubsetsTestCase(
            elements=["a", "b"],
            expected=[[], ["b"], ["a"], ["a", "b"]],
        ),
        SubsetsTestCase(
            elements=["a", "b", "c"],
            expected=[[], ["c"], ["b"], ["b", "c"], ["a"], ["a", "c"], ["a", "b"], ["a", "b", "c"]],
        ),
        SubsetsTestCase(
            elements=["x"],
            expected=[[], ["x"]],
        ),
        SubsetsTestCase(
            elements=[],
            expected=[[]],
        ),
        SubsetsTestCase(
            elements=["q", "r", "s", "t"],
            expected=[
                [],
                ["t"],
                ["s"],
                ["s", "t"],
                ["r"],
                ["r", "t"],
                ["r", "s"],
                ["r", "s", "t"],
                ["q"],
                ["q", "t"],
                ["q", "s"],
                ["q", "s", "t"],
                ["q", "r"],
                ["q", "r", "t"],
                ["q", "r", "s"],
                ["q", "r", "s", "t"],
            ],
        ),
    ]


def test_subsets(test_cases: list[SubsetsTestCase]) -> None:
    for t in test_cases:
        assert subsets(t.elements) == t.expected
