from pygments import highlight
from rich import screen, text
from ui.colors import HIGHLIGHT, RESET
from core import cursor
import random
import time
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
    
    def type_text(self, stdscr, row, text):

        for i in range(len(text) + 1):

            try:

                stdscr.addstr(
                    row,
                    0,
                    text[:i],
                    curses.color_pair(1)
                )

                stdscr.refresh()

                time.sleep(0.01)

            except curses.error:
                pass
    
    def crt_flicker(self, stdscr):

        import random
        import time

        if random.random() < 0.15:

            max_y, max_x = stdscr.getmaxyx()

            # lampeggio rapido
            stdscr.refresh()

            time.sleep(0.08)

            # crea disturbo casuale
            for _ in range(3):

                row = random.randint(
                    0,
                    max_y - 2
                )

                try:

                    stdscr.addstr(
                        row,
                        0,
                        " " * (max_x - 1),
                        curses.color_pair(1)
                    )

                except curses.error:
                    pass


            stdscr.refresh()

            time.sleep(0.05)