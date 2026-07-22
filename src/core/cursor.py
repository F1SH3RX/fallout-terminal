class Cursor:

    def __init__(self, screen, audio=None):

        self.screen = screen
        self.audio = audio
        self.row = 0
        self.column = 0


    def clamp(self):

        if self.row < 0:
            self.row = 0

        if self.row >= self.screen.rows:
            self.row = self.screen.rows - 1

        if self.column < 0:
            self.column = 0

        if self.column >= self.screen.columns:
            self.column = self.screen.columns - 1

    def play_move_sound(self):

        if self.audio:

            self.audio.play(
                "cursor.wav"
            )

    def move_left(self):

        element = self.current()

        if element:

            self.column = element.column - 1

        else:

            self.column -= 1
        self.play_move_sound()
        self.clamp()



    def move_right(self):

        element = self.current()

        if element:

            end = element.column + len(element.value)

            self.column = end

        else:

            self.column += 1

        self.play_move_sound()
        self.clamp()



    def move_up(self):

        self.row -= 1
        self.play_move_sound()
        self.clamp()



    def move_down(self):

        self.row += 1
        self.play_move_sound()
        self.clamp()



    def current(self):

        for element in self.screen.elements:

            if not element.active:
                continue

            if element.row != self.row:
                continue


            start = element.column

            end = start + len(element.value)


            if start <= self.column < end:

                return element


        return None