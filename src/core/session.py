from sys import path

from core.cursor import Cursor
from core.terminal import Terminal
from core.hacking import HackingGame
from core.generator import PuzzleGenerator
from core.screen_generator import ScreenGenerator
import random
import os
class Session:

    def __init__(self):

        self.words = self.load_dictionary()

        self.password = random.choice(self.words)

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

    def load_dictionary(self):

        path = "data/dictionaries/8.txt"

        with open(path, "r") as file:

            return [
                line.strip().upper()
                for line in file
                if line.strip()
            ]

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