"""A simple program with a function call."""  ##docstring (1) -- this lets a human read a code


def perimeter(length: float, width: float) -> float:
    """Calculates the perimeter of a rectangle."""  ##docstring (1)
    return (
        2 * length + 2 * width
    )  ##return statement (3) and use of a parameter's name in an expression (5) (in line 7)


## lines 4-8 are the function definition (4)

print(
    perimeter(length=10.0, width=8.0)
)  ##function call (2) and parameter's name in expression (5)
## print will take what is between parentheses and run it in the terminal-- it just shows output
## once python finds a function call, a bookmark is dropped and the return value replaces the function call statement once python evaluates the value
## any name in python is mapped to an address in your memory
