"""Exercise 3"""

__author__ = "730558323"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """inverts key with values"""
    new: dict[str, str] = {}
    for key in dictionary:
        k = dictionary[key]
        if k in new:
            raise KeyError("ERROR!")
        new[k] = key
    return new


def count(values: list[str]) -> dict[str, int]:
    """counts occurences of each value in list"""
    new: dict[str, int] = dict()
    for i in values:
        if i in new:
            new[i] += 1
        else:
            new[i] = 1
    return new


def favorite_color(colors: dict[str, str]) -> str:
    """finds most popular favorite color among a list of people's favorites"""
    listed_favs: list[str] = list()
    for i in colors:
        listed_favs.append(colors[i])
    counts = count(listed_favs)
    highest: int = 0
    fav_color: str = ""
    for color in counts:
        if counts[color] > highest:
            highest = counts[color]
            fav_color = color
    return fav_color


def bin_len(par: list[str]) -> dict[int, set[str]]:
    """returns strings in bins sorted by string length"""
    bins: dict[int, set[str]] = dict()
    for i in par:
        str_len = len(i)
        if str_len in bins:
            bins[str_len].add(i)
        else:
            bins[str_len] = {i}
    return bins
