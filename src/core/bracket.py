import random


class BracketAction:

    def __init__(self, terminal):
        self.terminal = terminal
        self.hacking_game = terminal.game
        self.screen = terminal.screen


    def activate(self, element):

        action = random.choice(
            [
                "REMOVE_DUD",
                "RESET_ATTEMPTS"
            ]
        )


        if action == "REMOVE_DUD":

            result = self.remove_dud()

        else:

            result = self.reset_attempts()


        element.active = False

        return result



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

        self.terminal.remove_word_element(dud)

        return f"DUD REMOVED: {dud}"



    def reset_attempts(self):

        self.hacking_game.attempts = 4

        return "TRIES RESET"