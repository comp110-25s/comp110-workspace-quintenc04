"""Wordle!"""

__author__ = "730558323"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    i = 1
    while i <= 6:
        print(f"=== Turn {i}/6 ===")
        input = input_guess(len(secret))
        print(emojified(input, secret))
        if input == secret:
            print(f"You won in {i}/6 turns!")
            return
        else:
            i += 1
        if i > 6:
            print("X/6 - Sorry, try again tomorrow!")


def contains_char(word: str, letter: str) -> bool:
    """determines if the secret word contains the guessed character"""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    i: int = 0  # recursion base case
    while i < len(
        word
    ):  # loops through each index in word str to check if the guessed letter is in it
        if word[i] == letter:
            return True
        i += 1  # relative reassignment operator
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Uses contains_char to test if guess letter is in secret word/correct position"""
    assert len(guess) == len(secret_word), "Guess must be same length as secret"
    emojis: str = ""  # an empty string to add the emojis to
    i: int = 0  # recursion base case
    while i < len(
        guess
    ):  # loops through each index in guess string to build a string of emojis
        if (
            contains_char(secret_word, guess[i]) is False
        ):  # current index of guess str matches no secret letters; white box returned
            emojis += WHITE_BOX
        elif (
            secret_word[i] == guess[i]
        ):  # if str at guess idx = str at secret word idx, guessed letter in right spot
            emojis += GREEN_BOX
        else:
            emojis += YELLOW_BOX
        i += 1
    return emojis  # returns fully buidl emojis string with len(guess) boxes


def input_guess(expected_length: int) -> str:
    """prompts user for guess until expected length is input"""
    response = input(
        f"Enter a {expected_length} character word: "
    )  # prompts user to input a response and assigns that response to a variable
    while (
        len(response) != expected_length
    ):  # continuously asks user for another input as long as the lengths do not match
        response = input(f"That wasn't {expected_length} chars! Try again: ")
    return response


if __name__ == "__main__":
    main(secret="codes")
