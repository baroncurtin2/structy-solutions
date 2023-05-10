from dataclasses import dataclass

import pytest

from structy.mixed_recall.tolerant_teams import RivalryList, tolerant_teams


@dataclass(slots=True)
class TolerantTeamsTestCase:
    rivalries: RivalryList
    expected: bool


@pytest.fixture
def test_cases() -> list[TolerantTeamsTestCase]:
    return [
        TolerantTeamsTestCase(
            rivalries=[
                ("philip", "seb"),
                ("raj", "nader"),
            ],
            expected=True,
        ),
        TolerantTeamsTestCase(
            rivalries=[
                ("philip", "seb"),
                ("raj", "nader"),
                ("raj", "philip"),
                ("seb", "raj"),
            ],
            expected=False,
        ),
        TolerantTeamsTestCase(
            rivalries=[
                ("cindy", "anj"),
                ("alex", "matt"),
                ("alex", "cindy"),
                ("anj", "matt"),
                ("brando", "matt"),
            ],
            expected=True,
        ),
        TolerantTeamsTestCase(
            rivalries=[
                ("alex", "anj"),
                ("alex", "matt"),
                ("alex", "cindy"),
                ("anj", "matt"),
                ("brando", "matt"),
            ],
            expected=False,
        ),
        TolerantTeamsTestCase(
            rivalries=[
                ("alan", "jj"),
                ("betty", "richard"),
                ("jj", "simcha"),
                ("richard", "christine"),
            ],
            expected=True,
        ),
        TolerantTeamsTestCase(
            rivalries=[
                ("alan", "jj"),
                ("betty", "richard"),
                ("jj", "simcha"),
                ("richard", "christine"),
            ],
            expected=True,
        ),
        TolerantTeamsTestCase(
            rivalries=[
                ("alan", "jj"),
                ("jj", "richard"),
                ("betty", "richard"),
                ("jj", "simcha"),
                ("richard", "christine"),
            ],
            expected=True,
        ),
        TolerantTeamsTestCase(
            rivalries=[
                ("alan", "jj"),
                ("betty", "richard"),
                ("betty", "christine"),
                ("jj", "simcha"),
                ("richard", "christine"),
            ],
            expected=False,
        ),
    ]


def test_tolerant_teams(test_cases: list[TolerantTeamsTestCase]) -> None:
    for tc in test_cases:
        assert tolerant_teams(tc.rivalries, recur=True) == tc.expected
        assert tolerant_teams(tc.rivalries, recur=False) == tc.expected
