import random

from core.screen import TerminalScreen
from core.noise import generate_noise


class ScreenGenerator:

    def __init__(self, rows=16, columns=32):
        self.rows = rows
        self.columns = columns


    def generate(self, words):

        screen = TerminalScreen(
            self.rows,
            self.columns
        )

        for row, word in enumerate(words):

            while True:

                column = random.randint(
                    2,
                    self.columns - len(word) - 3
                )

                if screen.can_place_word(
                    word,
                    row,
                    column
                ):
                    break

            screen.add_word(
                word,
                row,
                column
            )


        self.fill_noise(screen)

        return screen


    def fill_noise(self, screen):

        for row in range(screen.rows):

            for column in range(screen.columns):

                if screen.grid[row][column] == " ":

                    screen.grid[row][column] = (
                        generate_noise(1)
                    )