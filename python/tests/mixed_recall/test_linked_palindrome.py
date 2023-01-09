from dataclasses import dataclass

import pytest

from structy.mixed_recall.common import LinkedList
from structy.mixed_recall.linked_palindrome import linked_palindrome


@dataclass(slots=True)
class LinkedPalindromeTestCase:
    nums: list[int]
    expected: bool


@pytest.fixture
def test_cases() -> list[LinkedPalindromeTestCase]:
    return [
        LinkedPalindromeTestCase(
            nums=[3, 2, 7, 7, 2, 3],
            expected=True,
        ),
        LinkedPalindromeTestCase(
            nums=[3, 2, 4],
            expected=False,
        ),
        LinkedPalindromeTestCase(
            nums=[3, 2, 3],
            expected=True,
        ),
        LinkedPalindromeTestCase(
            nums=[0, 1, 0, 1, 0],
            expected=True,
        ),
        LinkedPalindromeTestCase(
            nums=[0, 1, 0, 1, 1],
            expected=False,
        ),
        LinkedPalindromeTestCase(
            nums=[5],
            expected=True,
        ),
        LinkedPalindromeTestCase(
            nums=[],
            expected=True,
        ),
    ]


def test_linked_palindrome(test_cases: list[LinkedPalindromeTestCase]) -> None:
    for t in test_cases:
        ll = LinkedList.from_values(t.nums)
        assert linked_palindrome(ll.head) == t.expected
