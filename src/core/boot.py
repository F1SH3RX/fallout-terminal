import time


class Boot:

    def __init__(self, audio):

        self.audio = audio

        self.finished = False

        self.lines = [
            "ROBCO INDUSTRIES (TM)",
            "",
            "UNIFIED OPERATING SYSTEM v1.0",
            "",
            "INITIALIZING TERMINAL...",
            "",
            "MEMORY CHECK",
            "SECURITY CHECK",
            "NETWORK LINK",
            "",
            "WELCOME OPERATOR"
        ]


    def run(self, renderer, stdscr):

        # suono accensione terminale
        self.audio.play(
            "boot.wav"
        )

        time.sleep(0.5)
        for line in self.lines:

            renderer.type_line(
                stdscr,
                line
            )

            time.sleep(0.4)


        renderer.loading_bar(
            stdscr
        )


        self.finished = True