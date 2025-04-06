"""File to define Bear class."""

__author__ = "730558323"


class Bear:
    """One Bear!"""
    age: int 
    hunger_score: int

    def __init__(self):
        """New Bear."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Simulates one day for bear."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Bear eats a fish."""
        self.hunger_score += num_fish
        return None
    