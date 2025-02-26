def guess_secret(word: str, secret: str, idx: int = 0) -> bool:
    if len(word) != len(secret):
        print("Words are different lengths.")
        return False
    if idx < len(word):  ## prevents infinite loop of checking for indices
        if word[idx] != secret[idx]:
            print(f"{word[idx]} isn't the word's next letter.")
            return False
        else:
            print(
                f"{word[idx]} is at index {idx} for both words! Checking next letters..."
            )
            return guess_secret(word=word, secret=secret, idx=idx + 1)  ## recursion
    print("They are the same word!")
    return True


print(guess_secret(word=input("What is your word?"), secret=SECRET))
