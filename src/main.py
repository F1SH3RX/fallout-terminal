from core.session import Session
from core.audio import AudioManager
from core.boot import Boot

from ui.boot_renderer import BootRenderer
from ui.renderer import TerminalRenderer

from core.menu import MainMenu
from ui.menu_renderer import MenuRenderer

from core.filesystem import FileSystem
from ui.filesystem_renderer import FileSystemRenderer

import curses
import time



def show_page(stdscr, lines):

    stdscr.clear()

    y = 3

    for line in lines:

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



# ======================
# FILE SYSTEM PHASE
# ======================

def filesystem_phase(stdscr, audio):

    filesystem = FileSystem(audio)

    renderer = FileSystemRenderer()


    while True:

        stdscr.clear()


        renderer.render(
            stdscr,
            filesystem
        )


        stdscr.refresh()


        key = stdscr.getch()



        # MOVIMENTO

        if key == curses.KEY_UP:

            filesystem.move_up()



        elif key == curses.KEY_DOWN:

            filesystem.move_down()



        # APERTURA FILE

        elif key in (10,13):

            audio.play(
                "select.wav"
            )


            content = filesystem.open()

            if isinstance(content, dict):

                if content["action"] == "shutdown":

                    stdscr.clear()


                    audio.play(
                        "error.wav"
                    )


                    stdscr.addstr(
                        10,
                        5,
                        "SYSTEM SHUTDOWN...",
                        curses.color_pair(1)
                    )


                    stdscr.refresh()


                    time.sleep(2)


                    return
            if content:

                stdscr.clear()


                y = 5


                for line in content:


                    audio.play(
                        "typing.wav"
                    )


                    stdscr.addstr(
                        y,
                        5,
                        line,
                        curses.color_pair(1)
                    )


                    stdscr.refresh()


                    time.sleep(0.05)


                    y += 1



                stdscr.addstr(
                    y + 2,
                    5,
                    "PRESS ANY KEY TO RETURN",
                    curses.color_pair(1)
                )


                stdscr.refresh()


                stdscr.getch()



        # ESC

        elif key == 27:

            filesystem.back()





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


    audio = AudioManager()


    boot = Boot(audio)


    boot_renderer = BootRenderer(
        audio=audio
    )



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


    menu = MainMenu(audio)


    menu_renderer = MenuRenderer()

    while True:

        audio.play(
            "menu.wav"
        )

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


                audio.play(
                    "select.wav"
                )



                action = menu.current_action()



                if action == "HACKING":

                    break



                elif action == "PAGE":


                    show_page(
                        stdscr,
                        menu.current_content()
                    )



                elif action == "EXIT":

                    return






        # ======================
        # HACKING TERMINAL LOADING
        # ======================


        stdscr.clear()



        loading_lines = [

            "ACCESSING SECURITY DATABASE...",

            "VERIFYING USER PRIVILEGES...",

            "LOADING ENCRYPTED FILES...",

            "INITIALIZING HACKING MODULE..."

        ]



        y = 5



        for line in loading_lines:


            audio.play(
                "radio_beep.wav"
            )



            stdscr.addstr(
                y,
                5,
                line,
                curses.color_pair(1)
            )


            stdscr.refresh()


            y += 1


            time.sleep(0.8)





        for i in range(18):


            if i % 2 == 0:

                audio.play(
                    "typing.wav"
                )



            stdscr.addstr(

                y,

                5,

                "[" + "#" * i + " " * (17-i) + "]",

                curses.color_pair(1)

            )


            stdscr.refresh()


            time.sleep(0.05)



        time.sleep(0.5)
        # ======================
        # HACKING SESSION
        # ======================


        session = Session(audio)


        renderer = TerminalRenderer(
            audio=audio
        )


        sound_played = False



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



                    before = line[
                        :start + OFFSET
                    ]



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

                            len(before)+len(word),

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
            # INFO PANEL
            # ======================


            try:


                info_y = len(output.split("\n")) + 1



                stdscr.addstr(

                    info_y,

                    0,

                    "PASSWORD ANALYSIS:",

                    curses.color_pair(1)

                )


                info_y += 1



                for word, result in session.history:


                    stdscr.addstr(

                        info_y,

                        0,

                        f"{word:<12} {result}",

                        curses.color_pair(1)

                    )


                    info_y += 1




                info_y += 1



                stdscr.addstr(

                    info_y,

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


                message_y = info_y + 2



                for i in range(3):


                    stdscr.addstr(

                        message_y+i,

                        0,

                        " "*(max_x-1),

                        curses.color_pair(1)

                    )




                for index, line in enumerate(

                    session.message.split("\n")

                ):


                    if message_y + index >= max_y:

                        break



                    stdscr.addstr(

                        message_y+index,

                        0,

                        line[:max_x-1],

                        curses.color_pair(1)

                    )



            except curses.error:

                pass





            renderer.crt_flicker(
                stdscr
            )


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



            elif key in (10,13):


                audio.play(
                    "select.wav"
                )


                session.select()



                if session.message:


                    stdscr.clear()



                    renderer.type_text(

                        stdscr,

                        25,

                        session.message

                    )



                    stdscr.refresh()


                    time.sleep(0.5)





            # ======================
            # END GAME
            # ======================


            if session.is_finished():



                # ======================
                # ACCESS GRANTED
                # ======================


                if session.game.success:



                    if not sound_played:


                        audio.play(
                            "access_granted.wav"
                        )


                        time.sleep(1)


                        audio.play(
                            "access_granted2_fast.wav"
                        )


                        sound_played = True




                    stdscr.clear()



                    stdscr.addstr(

                        10,

                        5,

                        "ACCESS GRANTED",

                        curses.color_pair(1)

                    )



                    stdscr.refresh()



                    time.sleep(2)




                    filesystem_phase(

                        stdscr,

                        audio

                    )



                    break






                # ======================
                # ACCESS DENIED
                # ======================


                elif session.game.locked:



                    if not sound_played:


                        audio.play(
                            "error.wav"
                        )


                        time.sleep(1)


                        audio.play(
                            "access_denied_fast.wav"
                        )


                        sound_played = True




                    stdscr.clear()



                    stdscr.addstr(

                        10,

                        5,

                        "ACCESS DENIED",

                        curses.color_pair(1)

                    )



                    stdscr.addstr(

                        12,

                        5,

                        "PRESS ANY KEY TO CONTINUE",

                        curses.color_pair(1)

                    )



                    stdscr.refresh()



                    stdscr.getch()



                    break
                continue




if __name__ == "__main__":


    curses.wrapper(main)