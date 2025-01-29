"""Computes the number of tea bags, number of treats, and cost
associated with a tea party, given the number of guests"""

__author__ = "730558323"


def main_planner(guests: int) -> None:
    """executes the above functions together"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """returns the number of tea bags based on the number of people"""
    return 2 * people


def treats(people: int) -> int:
    """returns number of treats based on number of teas"""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """returns cost based on treats and tea bags"""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
