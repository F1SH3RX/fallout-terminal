import os
import subprocess


class AudioManager:

    def __init__(self):

        self.path = "assets/sounds"


    def play(self, filename):

        try:

            sound_path = os.path.join(
                self.path,
                filename
            )

            subprocess.Popen(
                [
                    "aplay",
                    "-q",
                    sound_path
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )


        except Exception as e:

            print(
                f"AUDIO ERROR: {e}"
            )