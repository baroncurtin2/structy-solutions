from dataclasses import dataclass

import pytest

from structy.mixed_recall.max_increasing_subseq import max_increasing_subseq


@dataclass(slots=True)
class MaxIncreasingSubseqTestCase:
    numbers: list[int]
    expected: int


@pytest.fixture
def test_cases() -> list[MaxIncreasingSubseqTestCase]:
    return [
        MaxIncreasingSubseqTestCase(
            numbers=[4, 18, 20, 10, 12, 15, 19],
            expected=5,
        ),
        MaxIncreasingSubseqTestCase(
            numbers=[12, 9, 2, 5, 4, 32, 90, 20],
            expected=4,
        ),
        MaxIncreasingSubseqTestCase(
            numbers=[42, 50, 51, 60, 55, 70, 4, 5, 70],
            expected=5,
        ),
        MaxIncreasingSubseqTestCase(
            numbers=[7, 14, 10, 12],
            expected=3,
        ),
        MaxIncreasingSubseqTestCase(
            numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
            expected=21,
        ),
        MaxIncreasingSubseqTestCase(
            numbers=[
                1,
                2,
                3,
                4,
                5,
                12,
                6,
                30,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                10,
                18,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                100,
                104,
            ],
            expected=23,
        ),
        MaxIncreasingSubseqTestCase(
            numbers=[
                1,
                2,
                300,
                3,
                4,
                305,
                5,
                12,
                6,
                30,
                7,
                8,
                9,
                10,
                10,
                10,
                15,
                11,
                12,
                13,
                10,
                18,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                100,
                101,
                102,
                103,
                104,
                105,
            ],
            expected=27,
        ),
    ]


def test_max_increasing_subseq(test_cases: list[MaxIncreasingSubseqTestCase]) -> None:
    for tc in test_cases:
        assert max_increasing_subseq(tc.numbers) == tc.expected
        assert max_increasing_subseq(tc.numbers, recur=True) == tc.expected
