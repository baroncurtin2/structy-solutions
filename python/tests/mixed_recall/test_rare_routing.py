from dataclasses import dataclass

import pytest

from structy.graph.common import EdgeList
from structy.mixed_recall.rare_routing import rare_routing


@dataclass(slots=True)
class RareRoutingTestCase:
    n: int
    roads: EdgeList
    expected: bool


@pytest.fixture
def test_cases() -> list[RareRoutingTestCase]:
    return [
        RareRoutingTestCase(
            n=4,
            roads=[
                (0, 1),
                (0, 2),
                (0, 3),
            ],
            expected=True,
        ),
        RareRoutingTestCase(
            n=4,
            roads=[
                (0, 1),
                (0, 2),
                (0, 3),
                (3, 2),
            ],
            expected=False,
        ),
        RareRoutingTestCase(
            n=6,
            roads=[
                (1, 2),
                (5, 4),
                (3, 0),
                (0, 1),
                (0, 4),
            ],
            expected=True,
        ),
        RareRoutingTestCase(
            n=6,
            roads=[
                (1, 2),
                (4, 1),
                (5, 4),
                (3, 0),
                (0, 1),
                (0, 4),
            ],
            expected=False,
        ),
        RareRoutingTestCase(
            n=4,
            roads=[
                (0, 1),
                (3, 2),
            ],
            expected=False,
        ),
    ]


def test_rare_routing(test_cases: list[RareRoutingTestCase]) -> None:
    for tc in test_cases:
        assert rare_routing(tc.n, tc.roads, recur=True) == tc.expected
        assert rare_routing(tc.n, tc.roads) == tc.expected
