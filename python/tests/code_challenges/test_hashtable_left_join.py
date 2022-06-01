import pytest
from code_challenges.hashtable_left_join import hashmap_left_join


def test_exists():
    assert hashmap_left_join


# @pytest.mark.skip("TODO")
def test_example():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["diligent", "employed", "idle"],
        ["outfit", "garb", None],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["wrath", "anger", "delight"],
    ]

    actual = hashmap_left_join(synonyms, antonyms)

    assert actual == expected
