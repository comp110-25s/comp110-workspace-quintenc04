"""File to define Fish class."""

__author__ = "730558323"


class Fish:
    """One Fish!"""
    age: int
    
    def __init__(self):
        """New Fish."""
        self.age = 0
        return None
    
    def one_day(self):
        """Simulates one day for fish."""
        self.age += 1
        return None
