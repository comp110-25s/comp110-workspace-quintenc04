"""File to define River class."""

__author__ = "730558323"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """A River Ecosystem!"""
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks ages for fish and bears."""
        updated_fish: list[Fish] = []
        updated_bears: list[Bear] = []
        for f in self.fish:
            if f.age <= 3:
                updated_fish.append(f)
        for b in self.bears:
            if b.age <= 5:
                updated_bears.append(b)
        self.fish = updated_fish
        self.bears = updated_bears
        return None
    
    def remove_fish(self, amount: int):
        """Removes a fish from the river."""
        for _ in range(0, amount):
            self.fish.pop(0)
        return None

    def bears_eating(self):
        """Each bear eats 3 fish."""
        for b in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                b.eat(3)
        return None
    
    def check_hunger(self):
        """Checks hunger score for bears and removes those with low score."""
        updated_bears_1: list[Bear] = []
        for b in self.bears:
            if b.hunger_score >= 0:
                updated_bears_1.append(b)
        self.bears = updated_bears_1
        return None
        
    def repopulate_fish(self):
        """Adds four new fish for every fish pair."""
        fish_pairs: int = len(self.fish) // 2
        fish_offspring: int = fish_pairs * 4
        for _ in range(0, fish_offspring):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Adds one new bear for every bear pair."""
        bear_pairs: int = len(self.bears) // 2
        bear_offspring: int = bear_pairs
        for _ in range(0, bear_offspring):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Reports river populations on a day."""
        print(f"""
        ~~~ Day {self.day}: ~~~
        Fish population: {len(self.fish)}
        Bear population: {len(self.bears)}
        """)
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        for _ in range(0, 7):
            self.one_river_day()
        return None