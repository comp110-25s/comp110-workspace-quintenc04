"""Exercise 3 Test"""

import pytest

__author__ = "730558323"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_error_use() -> None:
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


def test_invert_use() -> None:
    assert invert({"1": "hi", "2": "hello"}) == {"hi": "1", "hello": "2"}


def test_invert_edge() -> None:
    assert invert({}) == {}


def test_count_use1() -> None:
    assert count(
        ["hello", "hi", "what's up", "hi", "hello", "greetings", "hello", "hey"]
    ) == {"hello": 3, "hi": 2, "what's up": 1, "greetings": 1, "hey": 1}


def test_count_use2() -> None:
    assert count(["beep"]) == {"beep": 1}


def test_count_edge() -> None:
    assert count([]) == {}


def test_favorite_color_use1() -> None:
    assert (
        favorite_color(
            {
                "Quinten": "Purple",
                "Kathryn": "Pink",
                "Ryder": "Blue",
                "Kyle": "Green",
                "Sawyer": "Blue",
            }
        )
        == "Blue"
    )


def test_favorite_color_use2() -> None:
    assert (
        favorite_color(
            {
                "Quinten": "Purple",
                "Kathryn": "Green",
                "Ryder": "Blue",
                "Kyle": "Green",
                "Sawyer": "Blue",
            }
        )
        == "Green"
    )


def test_favorite_color_edge() -> None:
    assert favorite_color({}) == ""


def test_bin_len_use1() -> None:
    assert bin_len(["goose", "ostrich", "penguin", "turkey", "bears", "otter"]) == {
        5: {"goose", "bears", "otter"},
        7: {"ostrich", "penguin"},
        6: {"turkey"},
    }


def test_bin_len_use2() -> None:
    assert bin_len(["bear", "fish", "bird", "frog"]) == {
        4: {"bear", "fish", "bird", "frog"}
    }


def test_bin_len_edge() -> None:
    assert bin_len([]) == {}
