import pytest

from app.randomizer import get_pairs

participants = {
    "Bob": "bob@dummy.com",
    "Sally": "sally@dummy.com",
    "Scott": "scott@dummy.com",
    "Jess": "jess@dummy.com",
    "Oliver": "oliver@dummy.com",
}

exclusions = {"Bob": "Sally", "Sally": "Bob", "Scott": "Jess, Oliver"}

too_many_exclusions = {
    "Bob": "Sally",
    "Sally": "Bob",
    "Scott": "Bob, Sally",
    "Jess": "Scott",
    "Oliver": "Bob, Sally",
}


def test_randomizer_can_find_pairs_successfully():
    pairs = get_pairs(participants, exclusions)
    assert len(pairs) == len(participants)
    for giver, receiver in pairs.items():
        assert receiver not in exclusions.get(giver, "")
    assert len(set(pairs.values())) == len(pairs.values())


def test_randomizer_fails_if_exclusions_prevent_pairs_matching():
    with pytest.raises(IndexError):
        get_pairs(participants, too_many_exclusions)
