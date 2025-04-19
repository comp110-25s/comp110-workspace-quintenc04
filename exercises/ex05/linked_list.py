"""Exercise 5!"""

from __future__ import annotations


__author__ = "730558323"


class Node:
    """Node in a singly-linked list recursive method."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Constructor!"""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Displays Node as string."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    """Finds value at a given index of a linked list."""
    if head is None or index < 0:
        raise IndexError("Index is out of bounds on the list.")
    elif index > 0:
        index -= 1
        n: Node | None = head.next
        return value_at(n, index)
    else:
        return head.value


def max(head: Node | None) -> int:
    """Finds max value in a linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    n: Node | None = head.next
    v: int = head.value
    if n is not None and n.value > v:
        v = n.value
        return max(n)
    else:
        return head.value


def linkify(items: list[int]) -> Node | None:
    """Turns a list into a linked list."""
    if len(items) == 0:
        return None
    elif len(items) == 1:
        return Node(items[0], None)
    else:
        n: Node | None = Node(items[0], linkify(items[1:]))
        return n


def scale(head: Node | None, factor: int) -> Node | None:
    """Multiplies every value in a linked list by given factor."""
    if head is None:
        return None
    new: Node | None = Node(head.value * factor, scale(head.next, factor))
    return new
