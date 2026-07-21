from pygments import highlight
from rich import screen
from ui.colors import HIGHLIGHT, RESET
from core import cursor
import curses

class TerminalRenderer:

    def __init__(self, start_address=0xF420):
        self.start_address = start_address


    def render(self, screen, cursor=None):

        output = []

        highlight = None

        for row in range(screen.rows):

            address = hex(
                self.start_address + row * 0x10
            )

            line = screen.get_line(row)


            if cursor:

                element = self.get_element_at(
                    screen,
                    cursor.row,
                    cursor.column
                )

                if element and element.row == row:

                    highlight = (
                        row,
                        element.column,
                        len(element.value)
                    )


            output.append(
                f"{address.upper()}  {line}"
            )


        return "\n".join(output), highlight
    
    def get_element_at(self, screen, row, column):

        for element in screen.elements:

            if not element.active:
                continue

            if element.row != row:
                continue

            start = element.column
            end = start + len(element.value)

            if start <= column < end:
                return element

        return None