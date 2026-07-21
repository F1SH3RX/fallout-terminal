from core.elements import TerminalElement
class TerminalScreen:

    def __init__(self, rows=16, columns=32):
        self.rows = rows
        self.columns = columns
        self.elements = []
        self.grid = [
            [" " for _ in range(columns)]
            for _ in range(rows)
        ]
        self.words = {}

    def add_word(self, word, row, column):

        for index, char in enumerate(word):
            self.set_character(
                row,
                column + index,
                char
            )

        self.words[word] = {
            "row": row,
            "column": column
        }
        self.elements.append(
            TerminalElement(
                value=word,
                element_type="WORD",
                row=row,
                column=column
            )
        )

    def set_character(self, row, column, char):
        if (
            0 <= row < self.rows
            and 0 <= column < self.columns
        ):
            self.grid[row][column] = char


    def get_line(self, row):
        return "".join(self.grid[row])


    def render(self):
        return "\n".join(
            self.get_line(row)
            for row in range(self.rows)
        )
    def can_place_word(self, word, row, column):

        if column + len(word) >= self.columns:
            return False

        for index in range(len(word)):

            if self.grid[row][column + index] != " ":
                return False

        return True
    
    def hide_element(self, element):

        for i in range(len(element.value)):

            self.grid[
                element.row
            ][
                element.column + i
            ] = "."