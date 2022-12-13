from dataclasses import dataclass

import pytest

from structy.graph.prereqs_possible import prereqs_possible_iter, prereqs_possible_recur


@dataclass(slots=True)
class PrereqsPossibleTestCase:
    num_courses: int
    pre_reqs: list[tuple[int, int]]
    expected: bool


@pytest.fixture
def test_cases() -> list[PrereqsPossibleTestCase]:
    return [
        PrereqsPossibleTestCase(
            num_courses=6,
            pre_reqs=[
                (0, 1),
                (2, 3),
                (0, 2),
                (1, 3),
                (4, 5),
            ],
            expected=True,
        ),
        PrereqsPossibleTestCase(
            num_courses=6,
            pre_reqs=[
                (0, 1),
                (2, 3),
                (0, 2),
                (1, 3),
                (4, 5),
                (3, 0),
            ],
            expected=False,
        ),
        PrereqsPossibleTestCase(
            num_courses=5,
            pre_reqs=[
                (2, 4),
                (1, 0),
                (0, 2),
                (0, 4),
            ],
            expected=True,
        ),
        PrereqsPossibleTestCase(
            num_courses=6,
            pre_reqs=[
                (2, 4),
                (1, 0),
                (0, 2),
                (0, 4),
                (5, 3),
                (3, 5),
            ],
            expected=False,
        ),
        PrereqsPossibleTestCase(
            num_courses=8,
            pre_reqs=[
                (1, 0),
                (0, 6),
                (2, 0),
                (0, 5),
                (3, 7),
                (4, 3),
            ],
            expected=True,
        ),
        PrereqsPossibleTestCase(
            num_courses=8,
            pre_reqs=[
                (1, 0),
                (0, 6),
                (2, 0),
                (0, 5),
                (3, 7),
                (7, 4),
                (4, 3),
            ],
            expected=False,
        ),
        PrereqsPossibleTestCase(
            num_courses=42,
            pre_reqs=[(6, 36)],
            expected=True,
        ),
    ]


def test_prereqs_possible_iter(test_cases):
    for t in test_cases:
        assert prereqs_possible_iter(t.num_courses, t.pre_reqs) == t.expected


def test_prereqs_possible_recur(test_cases):
    for t in test_cases:
        assert prereqs_possible_recur(t.num_courses, t.pre_reqs) == t.expected
