class TerminalScreen:

    def __init__(self, rows=16, columns=32):
        self.rows = rows
        self.columns = columns

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