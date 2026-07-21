import random

#from pygments.lexer import words

from core import screen
from core.screen import TerminalScreen
from core.noise import generate_noise
from core.brackets import generate_bracket
from core.elements import TerminalElement


class ScreenGenerator:

    def __init__(self, rows=16, columns=32):
        self.rows = rows
        self.columns = columns


    def generate(self, words):

        screen = TerminalScreen(
            self.rows,
            self.columns
        )


        for word in words:

            placed = False

            attempts = 0


            while not placed and attempts < 100:

                attempts += 1


                row = random.randint(
                    0,
                    self.rows - 1
                )


                column = random.randint(
                    2,
                    self.columns - len(word) - 2
                )


                if screen.can_place_word(
                    word,
                    row,
                    column
                ):

                    screen.add_word(
                        word,
                        row,
                        column
                    )

                    placed = True



        for _ in range(8):

            self.place_bracket(screen)



        self.fill_noise(screen)


        return screen


    def place_bracket(self, screen):

        bracket = generate_bracket()

        while True:

            row = random.randint(
                0,
                self.rows - 1
            )

            column = random.randint(
                0,
                self.columns - len(bracket) - 1
            )

            if screen.can_place_word(
                bracket,
                row,
                column
            ):
                break

        for index, char in enumerate(bracket):
            screen.set_character(
                row,
                column + index,
                char
            )

        screen.elements.append(
            TerminalElement(
                value=bracket,
                element_type="BRACKET",
                row=row,
                column=column
            )
        )

    def fill_noise(self, screen):

        for row in range(screen.rows):

            for column in range(screen.columns):

                if screen.grid[row][column] == " ":

                    screen.grid[row][column] = (
                        generate_noise(1)
                    )