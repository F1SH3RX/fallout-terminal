class GameSession:

    def __init__(self, terminal):

        self.terminal = terminal

        self.completed = False
        self.failed = False

    def update(self):

        game = self.terminal.game


        if game.success:
            self.completed = True

        elif game.locked:
            self.failed = True