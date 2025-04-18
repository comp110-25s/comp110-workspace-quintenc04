from __future__ import annotations


class Node:
    """Node in a singly-linked list recursive method"""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self):
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def last(head: Node) -> int:
    """prints last value in a linked list"""
    if head.next is None:
        return head.value
    else:
        return last(head.next)


def recursive_range(start: int, end: int) -> Node | None:
    """Create linked list with values from start to end (exclusive)."""
    if start < end:  # recursive case
        rest: Node | None = recursive_range(start=start + 1, end=end)
        return Node(start, rest)
    elif start == end:  # base case
        return None
    else:  # edge case
        raise Exception("start shouldn't be greater than end")
