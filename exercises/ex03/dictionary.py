"""Exercise 3"""

import pytest

__author__ = "730558323"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    new = {}
    for key in dictionary:
        k = dictionary[key]
        new[k] = key
    return new


with pytest.raises(KeyError):
    my_dictionary = {"kris": "jordan", "michael": "jordan"}
    invert(my_dictionary)

raise KeyError("ERROR!")
