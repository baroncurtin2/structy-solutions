from dataclasses import dataclass

import pytest

from structy.exhaustive_recursion.substitute_synonyms import substitute_synonyms


@dataclass(slots=True)
class SubstituteSynonymsTestCase:
    sentence: str
    synonyms: dict[str, list[str]]
    expected: list[str]


@pytest.fixture
def test_cases() -> list[SubstituteSynonymsTestCase]:
    return [
        SubstituteSynonymsTestCase(
            sentence="follow the yellow brick road",
            synonyms={
                "follow": ["chase", "pursue"],
                "yellow": ["gold", "amber", "lemon"],
            },
            expected=[
                "chase the gold brick road",
                "chase the amber brick road",
                "chase the lemon brick road",
                "pursue the gold brick road",
                "pursue the amber brick road",
                "pursue the lemon brick road",
            ],
        ),
        SubstituteSynonymsTestCase(
            sentence="I think it's gonna be a long long time",
            synonyms={
                "think": ["believe", "reckon"],
                "long": ["lengthy", "prolonged"],
            },
            expected=[
                "I believe it's gonna be a lengthy lengthy time",
                "I believe it's gonna be a lengthy prolonged time",
                "I believe it's gonna be a prolonged lengthy time",
                "I believe it's gonna be a prolonged prolonged time",
                "I reckon it's gonna be a lengthy lengthy time",
                "I reckon it's gonna be a lengthy prolonged time",
                "I reckon it's gonna be a prolonged lengthy time",
                "I reckon it's gonna be a prolonged prolonged time",
            ],
        ),
        SubstituteSynonymsTestCase(
            sentence="palms sweaty knees weak arms heavy",
            synonyms={
                "palms": ["hands", "fists"],
                "heavy": ["weighty", "hefty", "burdensome"],
                "weak": ["fragile", "feeble", "frail", "sickly"],
            },
            expected=[
                "hands sweaty knees fragile arms weighty",
                "hands sweaty knees fragile arms hefty",
                "hands sweaty knees fragile arms burdensome",
                "hands sweaty knees feeble arms weighty",
                "hands sweaty knees feeble arms hefty",
                "hands sweaty knees feeble arms burdensome",
                "hands sweaty knees frail arms weighty",
                "hands sweaty knees frail arms hefty",
                "hands sweaty knees frail arms burdensome",
                "hands sweaty knees sickly arms weighty",
                "hands sweaty knees sickly arms hefty",
                "hands sweaty knees sickly arms burdensome",
                "fists sweaty knees fragile arms weighty",
                "fists sweaty knees fragile arms hefty",
                "fists sweaty knees fragile arms burdensome",
                "fists sweaty knees feeble arms weighty",
                "fists sweaty knees feeble arms hefty",
                "fists sweaty knees feeble arms burdensome",
                "fists sweaty knees frail arms weighty",
                "fists sweaty knees frail arms hefty",
                "fists sweaty knees frail arms burdensome",
                "fists sweaty knees sickly arms weighty",
                "fists sweaty knees sickly arms hefty",
                "fists sweaty knees sickly arms burdensome",
            ],
        ),
    ]


def test_substitute_synonyms(test_cases: list[SubstituteSynonymsTestCase]) -> None:
    for t in test_cases:
        assert substitute_synonyms(t.sentence, t.synonyms) == t.expected
