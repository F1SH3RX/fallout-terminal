from pathlib import Path


def load_words(length):

    path = Path(
        f"data/dictionaries/{length}.txt"
    )

    with open(path, "r") as file:
        return [
            word.strip().upper()
            for word in file.readlines()
        ]