import curses


class FileSystemRenderer:


    def render(
        self,
        stdscr,
        filesystem
    ):

        stdscr.clear()


        stdscr.addstr(
            2,
            5,
            "ROBCO INDUSTRIES TERMINAL",
            curses.color_pair(1)
        )


        stdscr.addstr(
            4,
            5,
            "MAINFRAME FILE SYSTEM",
            curses.color_pair(1)
        )
        stdscr.addstr(
                    6,
                    5,
                    "PRESS ESC TO GO BACK",
                    curses.color_pair(1)
                )

        y = 9


        for index,item in enumerate(filesystem.current):


            prefix = "> " if index == filesystem.selected else "  "


            symbol = (
                "[DIR]"
                if item["type"]=="folder"
                else "[FILE]"
            )


            stdscr.addstr(
                y,
                5,
                f"{prefix}{symbol} {item['name']}",
                curses.color_pair(1)
            )


            y += 1


        stdscr.refresh()