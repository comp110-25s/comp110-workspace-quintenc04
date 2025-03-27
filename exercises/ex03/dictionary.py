"""Exercise 3"""

import pytest

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
    listed_favs: list[str] = list()
    for i in colors:
        listed_favs.append(colors[i])
    counts = count(listed_favs)
    idx: int = 0
    highest: list[int] = list()
    for i in counts:
        if idx == 0:
            highest.append(counts[i])
        if 0 < idx < len(counts):
            if counts[i] > highest[idx - 1]:
                highest[idx - 1] = counts[i]
        idx += 1
    for i in counts:
        if highest == counts[i]:
            return i


def favorite_color(colors: dict[str, str]) -> str:
    listed_favs: list[str] = list()
    for i in colors:
        listed_favs.append(colors[i])
    counts = count(listed_favs)
    highest: int = 0
    fav_color: str = ""
    for color in counts:
        if counts[color] > highest:
            highest = counts[color]
            favorite = color
    return favorite


def bin_len(par: list[str]) -> dict[int, set[str]]:
    bins: dict[int, set[str]] = dict()
    for i in par:
        str_len = len(i)
        if str_len in bins:
            bins[str_len].add(i)
        else:
            bins[str_len] = {i}
    return bins
