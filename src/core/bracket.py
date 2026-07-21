import random


class BracketAction:

    def __init__(self, hacking_game):
        self.hacking_game = hacking_game


    def activate(self):

        action = random.choice(
            [
                "REMOVE_DUD",
                "RESET_ATTEMPTS"
            ]
        )


        if action == "REMOVE_DUD":

            return self.remove_dud()


        if action == "RESET_ATTEMPTS":

            return self.reset_attempts()


    def remove_dud(self):

        words = [
            word
            for word in self.hacking_game.words
            if word != self.hacking_game.password
    ]


        if len(words) == 0:
            return "NO DUD AVAILABLE"


        dud = random.choice(words)

        self.hacking_game.words.remove(dud)

        return f"DUD REMOVED: {dud}"


    def reset_attempts(self):

        self.hacking_game.attempts = 4

        return "TRIES RESET"