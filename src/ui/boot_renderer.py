import curses
from pydoc import text
import time

class BootRenderer:



    def draw_logo(self, stdscr):

        stdscr.clear()

        logo = r"""
███████╗ █████╗ ██╗     ██╗      ██████╗ ██╗   ██╗████████╗
██╔════╝██╔══██╗██║     ██║     ██╔═══██╗██║   ██║╚══██╔══╝
█████╗  ███████║██║     ██║     ██║   ██║██║   ██║   ██║
██╔══╝  ██╔══██║██║     ██║     ██║   ██║██║   ██║   ██║
██║     ██║  ██║███████╗███████╗╚██████╔╝╚██████╔╝   ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝  ╚═════╝    ╚═╝
"""


        y = 2


        for line in logo.split("\n"):

            stdscr.addstr(
                y,
                2,
                ""
            )

            for char in line:

                stdscr.addch(
                    char,
                    curses.color_pair(1)
                )

                stdscr.refresh()

                time.sleep(0.002)


            y += 1


        time.sleep(1)

    def type_line(self, stdscr, text):

        y, x = stdscr.getyx()

        for char in text:

            stdscr.addch(
                char,
                curses.color_pair(1)
            )

            stdscr.refresh()

            time.sleep(0.03)

        stdscr.addch("\n")
        stdscr.refresh()

    def loading_bar(self, stdscr):

        stdscr.addstr(
            "\nLOADING SYSTEM: ["
        )

        stdscr.refresh()


        for i in range(20):

            stdscr.addstr(
                "#",
                curses.color_pair(1)
            )

            stdscr.refresh()

            time.sleep(0.08)


        stdscr.addstr("]\n")

        stdscr.refresh()

        time.sleep(1)

    def draw(self, stdscr, boot):

        stdscr.clear()


        y = 1


        for line in self.FALLOUT.split("\n"):

            stdscr.addstr(
                y,
                2,
                line,
                curses.color_pair(1)
            )

            y += 1


        y += 1


        for i in range(boot.index):

            line = boot.lines[i]


            if "CHECK" in line or "LINK" in line:

                if "MEMORY" in line:
                    line = (
                        "MEMORY CHECK ........ "
                        "[##########] OK"
                    )

                elif "SECURITY" in line:
                    line = (
                        "SECURITY CHECK ...... "
                        "[##########] OK"
                    )

                elif "NETWORK" in line:
                    line = (
                        "NETWORK LINK ........ "
                        "[##########] OK"
                    )


            stdscr.addstr(
                y,
                5,
                line,
                curses.color_pair(1)
            )

            y += 1


        stdscr.refresh()