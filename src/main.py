from core.session import Session
from core.boot import Boot
from ui import menu
from ui import menu_renderer
from ui.boot_renderer import BootRenderer
from ui.renderer import TerminalRenderer
from core.menu import MainMenu
from ui.menu_renderer import MenuRenderer
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


    # ======================
    # BOOT SCREEN
    # ======================

    boot = Boot()
    boot_renderer = BootRenderer()


    stdscr.clear()

    boot_renderer.draw_logo(
        stdscr
    )


    boot.run(
        boot_renderer,
        stdscr
    )


    stdscr.addstr(
        "\nPRESS ANY KEY TO CONTINUE",
        curses.color_pair(1)
    )

    stdscr.refresh()

    stdscr.getch()

    # ======================
    # MENU
    # ======================

    menu = MainMenu()

    menu_renderer = MenuRenderer()


    while True:

        menu_renderer.render(
            stdscr,
            menu
        )


        key = stdscr.getch()


        if key == curses.KEY_UP:

            menu.move_up()


        elif key == curses.KEY_DOWN:

            menu.move_down()


        elif key in (10,13):

            if menu.current() == "ACCESS SECURITY SYSTEM":
                break

            elif menu.current() == "SYSTEM INFORMATION":

                stdscr.clear()


                y = 3

                for line in menu.get_information():

                    stdscr.addstr(
                        y,
                        5,
                        line,
                        curses.color_pair(1)
                    )

                    y += 1


                stdscr.addstr(
                    y + 2,
                    5,
                    "PRESS ANY KEY TO RETURN",
                    curses.color_pair(1)
                )


                stdscr.refresh()

                stdscr.getch()

            elif menu.current() == "SHUTDOWN":
                return

    # ======================
    # HACKING TERMINAL
    # ======================

    session = Session()

    renderer = TerminalRenderer()



    while True:

        stdscr.clear()

        max_y, max_x = stdscr.getmaxyx()


        output, highlight = renderer.render(
            session.screen,
            session.cursor
        )


        for row, line in enumerate(
            output.split("\n")
        ):

            if row >= max_y:
                break



            # ======================
            # HIGHLIGHT ELEMENT
            # ======================

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
                        before[:max_x-1],
                        curses.color_pair(1)
                    )


                    stdscr.addstr(
                        row,
                        len(before),
                        word[:max_x-len(before)-1],
                        curses.color_pair(1) | curses.A_REVERSE
                    )


                    stdscr.addstr(
                        row,
                        len(before) + len(word),
                        after[:max_x-len(before)-len(word)-1],
                        curses.color_pair(1)
                    )


                except curses.error:
                    pass



            # ======================
            # NORMAL LINE
            # ======================

            else:

                try:

                    stdscr.addstr(
                        row,
                        0,
                        line[:max_x-1],
                        curses.color_pair(1)
                    )


                except curses.error:
                    pass




        # ======================
        # ATTEMPTS
        # ======================

        try:

            stdscr.addstr(
                23,
                0,
                f"Attempts remaining: {session.game.attempts}",
                curses.color_pair(1)
            )


        except curses.error:
            pass




        # ======================
        # RESULT MESSAGE
        # ======================

        try:

            stdscr.addstr(
                25,
                0,
                " " * (max_x - 1),
                curses.color_pair(1)
            )


            for index, line in enumerate(
                session.message.split("\n")
            ):

                if 25 + index >= max_y:
                    break


                stdscr.addstr(
                    25 + index,
                    0,
                    line[:max_x-1],
                    curses.color_pair(1)
                )


        except curses.error:
            pass



        renderer.crt_flicker(stdscr)
        stdscr.refresh()


        key = stdscr.getch()



        # ======================
        # INPUT
        # ======================

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

            if session.message:

                stdscr.clear()

                renderer.type_text(
                    stdscr,
                    19,
                    session.message
                )

                stdscr.refresh()



        # ======================
        # END GAME
        # ======================

        if session.is_finished():

            try:

                stdscr.addstr(
                    27,
                    0,
                    session.message,
                    curses.color_pair(1)
                )


                stdscr.addstr(
                    28,
                    0,
                    "PRESS ANY KEY TO CONTINUE",
                    curses.color_pair(1)
                )


            except curses.error:
                pass


            stdscr.refresh()

            stdscr.getch()

            break



if __name__ == "__main__":

    curses.wrapper(main)