from dataclasses import dataclass

import pytest

from structy.dynamic_programming.array_stepper import array_stepper


@dataclass(slots=True)
class ArrayStepperTestCase:
    numbers: list[int]
    expected: bool


@pytest.fixture
def test_cases() -> list[ArrayStepperTestCase]:
    return [
        ArrayStepperTestCase(
            numbers=[2, 4, 2, 0, 0, 1],
            expected=True,
        ),
        ArrayStepperTestCase(
            numbers=[2, 3, 2, 0, 0, 1],
            expected=False,
        ),
        ArrayStepperTestCase(
            numbers=[3, 1, 3, 1, 0, 1],
            expected=True,
        ),
        ArrayStepperTestCase(
            numbers=[4, 1, 5, 1, 1, 1, 0, 4],
            expected=True,
        ),
        ArrayStepperTestCase(
            numbers=[4, 1, 2, 1, 1, 1, 0, 4],
            expected=False,
        ),
        ArrayStepperTestCase(
            numbers=[1, 1, 1, 1, 1, 0],
            expected=True,
        ),
        ArrayStepperTestCase(
            numbers=[1, 1, 1, 1, 0, 0],
            expected=False,
        ),
        ArrayStepperTestCase(
            numbers=[
                31,
                30,
                29,
                28,
                27,
                26,
                25,
                24,
                23,
                22,
                21,
                20,
                19,
                18,
                17,
                16,
                15,
                14,
                13,
                12,
                11,
                10,
                9,
                8,
                7,
                6,
                5,
                3,
                2,
                1,
                0,
                0,
                0,
            ],
            expected=False,
        ),
    ]


def test_array_stepper(test_cases):
    for t in test_cases:
        assert array_stepper(t.numbers) == t.expected
