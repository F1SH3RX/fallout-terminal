import os
os.environ["SDL_AUDIODRIVER"] = "alsa"
import pygame


class AudioManager:

    def __init__(self):

        self.path = "assets/sounds"
        os.environ["ALSA_PCM_CARD"] = "1"
        print("AUDIO INIT:", pygame.mixer.get_init())
        pygame.mixer.init(
            frequency=44100,
            size=-16,
            channels=2,
            buffer=512
        )

        self.sounds = {}

        self.load_sounds()


    def load_sounds(self):

        for filename in os.listdir(self.path):

            if filename.endswith(".wav"):

                path = os.path.join(
                    self.path,
                    filename
                )

                try:

                    self.sounds[filename] = pygame.mixer.Sound(path)

                    print(
                        f"Loaded sound: {filename}"
                    )

                except Exception as e:

                    print(
                        f"AUDIO LOAD ERROR {filename}: {e}"
                    )


    def play(self, filename):

        try:

            sound = self.sounds.get(filename)

            if sound:

                sound.play()

            else:

                print(
                    f"SOUND NOT FOUND: {filename}"
                )


        except Exception as e:

            print(
                f"AUDIO ERROR: {e}"
            )
