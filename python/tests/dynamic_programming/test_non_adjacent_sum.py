from dataclasses import dataclass

import pytest

from structy.dynamic_programming.non_adjacent_sum import non_adjacent_sum


@dataclass(slots=True)
class NonAdjacentSumTestCase:
    nums: list[int]
    expected: int


@pytest.fixture
def test_cases() -> list[NonAdjacentSumTestCase]:
    return [
        NonAdjacentSumTestCase(
            nums=[2, 4, 5, 12, 7],
            expected=16,
        ),
        NonAdjacentSumTestCase(
            nums=[7, 5, 5, 12],
            expected=19,
        ),
        NonAdjacentSumTestCase(
            nums=[7, 5, 5, 12, 17, 29],
            expected=48,
        ),
        NonAdjacentSumTestCase(
            nums=[
                72,
                62,
                10,
                6,
                20,
                19,
                42,
                46,
                24,
                78,
                30,
                41,
                75,
                38,
                23,
                28,
                66,
                55,
                12,
                17,
                9,
                12,
                3,
                1,
                19,
                30,
                50,
                20,
            ],
            expected=488,
        ),
        NonAdjacentSumTestCase(
            nums=[
                72,
                62,
                10,
                6,
                20,
                19,
                42,
                46,
                24,
                78,
                30,
                41,
                75,
                38,
                23,
                28,
                66,
                55,
                12,
                17,
                83,
                80,
                56,
                68,
                6,
                22,
                56,
                96,
                77,
                98,
                61,
                20,
                0,
                76,
                53,
                74,
                8,
                22,
                92,
                37,
                30,
                41,
                75,
                38,
                23,
                28,
                66,
                55,
                12,
                17,
                72,
                62,
                10,
                6,
                20,
                19,
                42,
                46,
                24,
                78,
                42,
            ],
            expected=1465,
        ),
    ]


def test_non_adjacent_sum(test_cases):
    for t in test_cases:
        assert non_adjacent_sum(t.nums) == t.expected
