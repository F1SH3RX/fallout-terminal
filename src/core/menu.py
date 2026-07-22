import json


class MainMenu:

    def __init__(self, audio=None):

        self.audio = audio

        with open(
            "data/config/menu.json",
            "r"
        ) as file:

            data = json.load(file)


        self.title_text = data.get(
            "title",
            "ROBCO INDUSTRIES TERMINAL"
        )


        self.options = data["options"]

        self.selected = 0



    def play_move_sound(self):

        if self.audio:

            self.audio.play(
                "cursor.wav"
            )



    def move_up(self):

        self.selected -= 1

        if self.selected < 0:

            self.selected = len(self.options) - 1

        self.play_move_sound()



    def move_down(self):

        self.selected += 1

        if self.selected >= len(self.options):

            self.selected = 0

        self.play_move_sound()



    def current(self):

        return self.options[self.selected]["name"]



    def current_action(self):

        return self.options[self.selected]["action"]



    def current_content(self):

        return self.options[self.selected].get(
            "content",
            []
        )


    def title(self):

        return self.title_text