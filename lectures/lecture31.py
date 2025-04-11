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
        
courses: Node = Node(110, Node(210, Node(211, None)))
print(courses)

def last(head: Node) -> int:
    """prints last value in a linked list"""
    if head.next is None:
        return head.value
    else:
        return last(head.next)
    
last(courses)