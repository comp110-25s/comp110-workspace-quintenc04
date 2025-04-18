from __future__ import annotations
from lectures.lecture32 import Node

"""Exercise 5!"""

__author__ = "730558323"


def value_at(head: Node | None, index: int) -> int:
    "Finds value at a given index of a linked list."
    if index > 0:
        index -= 1
        n = head
    elif index == 0:
        return n.value
    else:
        raise IndexError("Index is out of bounds on the list.")
