from core.cursor import Cursor
from core.terminal import Terminal
from core.hacking import HackingGame
from core.generator import PuzzleGenerator
from core.screen_generator import ScreenGenerator


class Session:

    def __init__(self):

        self.words = [
            "OVERSEER",
            "SECURITY",
            "DIRECTOR",
            "FACILITY"
        ]

        self.password = "OVERSEER"


        generator = PuzzleGenerator(
            self.password,
            self.words
        )

        puzzle_words = generator.generate()


        screen_generator = ScreenGenerator()

        self.screen = screen_generator.generate(
            puzzle_words
        )


        self.game = HackingGame(
            self.password,
            puzzle_words
        )


        self.terminal = Terminal(
            self.game,
            self.screen
        )


        self.cursor = Cursor(
            self.screen
        )


        self.terminal.cursor = self.cursor


        self.message = ""


    def select(self):

        result = self.terminal.select_cursor()

        if result:
            self.message = result

        if self.game.success or self.game.locked:

            self.finished = True

    def is_finished(self):

        return (
            self.game.success
            or self.game.locked
        )