"""Wordle!"""

__author__ = "730558323"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, letter: str) -> bool:
    """determines if the secret word contains the guessed character"""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    i: int = 0
    while i < len(word):
        if word[i] == letter:
            return True
        i += 1  # relative reassignment operator
    return False


def emojified(guess: str, secret: str) -> str:
    """Uses contains_char to test if guess letter is in secret word/correct position"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    emojis: str = ""
    i: int = 0
    while i < len(guess):
        if contains_char(secret, guess[i]) is False:
            emojis += WHITE_BOX
        elif secret[i] == guess[i]:
            emojis += GREEN_BOX
        else:
            emojis += YELLOW_BOX
        i += 1
    return emojis


def input_guess(expected_length: int) -> str:
    """prompts user for guess until expected length is input"""
    response = input(f"Enter a {expected_length} character word: ")
    if len(response) == expected_length:
        return "response"
    else:
        response = input("That wasn't {expected_length} chars! Try again: ")
        return response
