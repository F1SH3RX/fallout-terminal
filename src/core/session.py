class GameSession:

    def __init__(self, terminal):

        self.terminal = terminal

        self.completed = False
        self.failed = False

    def check_state(self):

        if self.terminal.game.finished:

            if self.terminal.game.attempts > 0:
                self.completed = True

            else:
                self.failed = True