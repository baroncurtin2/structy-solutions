from dataclasses import dataclass

import pytest

from structy.graph.common import EdgeList
from structy.graph.semesters_required import semesters_required_dfs, semesters_required_recur


@dataclass(slots=True)
class SemestersRequiredTestCase:
    num_courses: int
    pre_reqs: EdgeList
    expected: int


@pytest.fixture
def test_cases() -> list[SemestersRequiredTestCase]:
    return [
        SemestersRequiredTestCase(
            num_courses=6,
            pre_reqs=[
                (1, 2),
                (2, 4),
                (3, 5),
                (0, 5),
            ],
            expected=3,
        ),
        SemestersRequiredTestCase(
            num_courses=7,
            pre_reqs=[
                (4, 3),
                (3, 2),
                (2, 1),
                (1, 0),
                (5, 2),
                (5, 6),
            ],
            expected=5,
        ),
        SemestersRequiredTestCase(
            num_courses=5,
            pre_reqs=[
                (1, 0),
                (3, 4),
                (1, 2),
                (3, 2),
            ],
            expected=2,
        ),
        SemestersRequiredTestCase(
            num_courses=12,
            pre_reqs=[],
            expected=1,
        ),
        SemestersRequiredTestCase(
            num_courses=3,
            pre_reqs=[
                (0, 2),
                (0, 1),
                (1, 2),
            ],
            expected=3,
        ),
        SemestersRequiredTestCase(
            num_courses=6,
            pre_reqs=[
                (3, 4),
                (3, 0),
                (3, 1),
                (3, 2),
                (3, 5),
            ],
            expected=2,
        ),
    ]


def test_semesters_required_dfs(test_cases):
    for t in test_cases:
        assert semesters_required_dfs(t.num_courses, t.pre_reqs) == t.expected


def test_semesters_required_recur(test_cases):
    for t in test_cases:
        assert semesters_required_recur(t.num_courses, t.pre_reqs) == t.expected
