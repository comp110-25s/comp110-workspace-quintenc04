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
            print(f"You won in {i} turns!")
        else:
            i += 1
        if i >= 7:
            print("X/6 - Sorry, try again tomorrow!")


def contains_char(word: str, letter: str) -> bool:
    """determines if the secret word contains the guessed character"""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    i: int = 0
    while i < len(word):
        if word[i] == letter:
            return True
        i += 1  # relative reassignment operator
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Uses contains_char to test if guess letter is in secret word/correct position"""
    assert len(guess) == len(secret_word), "Guess must be same length as secret"
    emojis: str = ""
    i: int = 0
    while i < len(guess):
        if contains_char(secret_word, guess[i]) is False:
            emojis += WHITE_BOX
        elif secret_word[i] == guess[i]:
            emojis += GREEN_BOX
        else:
            emojis += YELLOW_BOX
        i += 1
    return emojis


def input_guess(expected_length: int) -> str:
    """prompts user for guess until expected length is input"""
    response = input(f"Enter a {expected_length} character word: ")
    while len(response) != expected_length:
        response = input(f"That wasn't {expected_length} chars! Try again: ")
    return response


if __name__ == "__main__":
    main(secret="codes")
