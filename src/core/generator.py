import random


class PuzzleGenerator:

    def __init__(self, password, words):
        if password not in words:
            raise ValueError(
                "Password not found in dictionary"
            )
        self.password = password
        self.words = words


    def generate(self):
        candidates = [
            word for word in self.words
            if len(word) == len(self.password)
        ]

        selected = random.sample(
            candidates,
            min(5, len(candidates))
        )

        if self.password not in selected:
            selected.append(self.password)

        random.shuffle(selected)

        return selected
    
    def get_password(self):
        return self.password