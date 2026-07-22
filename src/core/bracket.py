import random

from core import audio


class BracketAction:

    def __init__(self, terminal, audio=None):
        self.terminal = terminal
        self.hacking_game = terminal.game
        self.screen = terminal.screen
        self.audio = audio

    def activate(self, element):

        action = random.choice(
            [
                "REMOVE_DUD",
                "RESET_ATTEMPTS"
            ]
        )
        if self.audio:

            self.audio.play(
                "bracket.wav"
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