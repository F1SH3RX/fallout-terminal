class Terminal:

    def __init__(
        self,
        game,
        screen
    ):
        self.game = game
        self.screen = screen


    def attempt(self, word):

        result = self.game.guess(word)

        return result