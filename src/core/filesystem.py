import json


class FileSystem:


    def __init__(self, audio=None):

        self.audio = audio


        with open(
            "data/config/filesystem.json",
            "r"
        ) as file:

            data = json.load(file)


        self.root = data["root"]

        self.current = self.root

        self.path = []

        self.selected = 0



    def move_up(self):

        self.selected -= 1

        if self.selected < 0:

            self.selected = len(self.current)-1


        if self.audio:

            self.audio.play(
                "cursor.wav"
            )



    def move_down(self):

        self.selected += 1

        if self.selected >= len(self.current):

            self.selected = 0


        if self.audio:

            self.audio.play(
                "cursor.wav"
            )



    def current_item(self):

        return self.current[self.selected]



    def open(self):

        item = self.current_item()


        if self.audio:

            self.audio.play(
                "select.wav"
            )


        # CARTELLA

        if item["type"] == "folder":

            self.path.append(
                self.current
            )

            self.current = item["children"]

            self.selected = 0

            return None



        # FILE

        elif item["type"] == "file":

            return item["content"]



        # AZIONE

        elif item["type"] == "action":

            return {
                "action": item["action"]
            }

    def back(self):

        if self.path:

            self.current = self.path.pop()

            self.selected = 0