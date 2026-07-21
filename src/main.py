from core.session import Session
from ui.renderer import TerminalRenderer
import curses


def main(stdscr):

    curses.curs_set(0)
    stdscr.keypad(True)
    stdscr.clear()

    curses.start_color()

    curses.init_pair(
        1,
        curses.COLOR_GREEN,
        curses.COLOR_BLACK
    )


    session = Session()

    renderer = TerminalRenderer()


    while True:

        stdscr.clear()

        max_y, max_x = stdscr.getmaxyx()


        output, highlight = renderer.render(
            session.screen,
            session.cursor
        )


        for row, line in enumerate(output.split("\n")):

            if row >= max_y:
                break


            if highlight and highlight[0] == row:

                _, start, length = highlight

                OFFSET = 8


                before = line[:start + OFFSET]

                word = line[
                    start + OFFSET:
                    start + OFFSET + length
                ]

                after = line[
                    start + OFFSET + length:
                ]


                try:

                    stdscr.addstr(
                        row,
                        0,
                        before[:max_x-1]
                    )

                    stdscr.addstr(
                        row,
                        len(before),
                        word[:max_x-len(before)-1],
                        curses.A_REVERSE
                    )

                    stdscr.addstr(
                        row,
                        len(before) + len(word),
                        after[:max_x-len(before)-len(word)-1]
                    )

                except curses.error:
                    pass


            else:

                try:

                    stdscr.addstr(
                        row,
                        0,
                        line[:max_x-1]
                    )

                except curses.error:
                    pass



        # Tentativi

        try:

            stdscr.addstr(
                17,
                0,
                f"Attempts: {session.game.attempts}"
            )

        except curses.error:
            pass



        # Messaggio risultato

        try:

            stdscr.addstr(
                19,
                0,
                " " * (max_x - 1)
            )


            for index, line in enumerate(
                session.message.split("\n")
            ):

                if 19 + index >= max_y:
                    break


                stdscr.addstr(
                    19 + index,
                    0,
                    line[:max_x-1],
                    curses.color_pair(1)
                )

        except curses.error:
            pass



        stdscr.refresh()


        key = stdscr.getch()



        if key == ord("q"):

            break


        elif key == curses.KEY_UP:

            session.cursor.move_up()


        elif key == curses.KEY_DOWN:

            session.cursor.move_down()


        elif key == curses.KEY_LEFT:

            session.cursor.move_left()


        elif key == curses.KEY_RIGHT:

            session.cursor.move_right()


        elif key in (10, 13):

            session.select()



        if session.is_finished():
            stdscr.addstr(
                21,
                0,
                session.message
            )
            
            stdscr.addstr(
                22,
                0,
                "PRESS ANY KEY TO CONTINUE"
            )

            stdscr.refresh()

            stdscr.getch()

            break



if __name__ == "__main__":

    curses.wrapper(main)