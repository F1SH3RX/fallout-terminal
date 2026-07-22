from core.audio import AudioManager
import time

audio = AudioManager()

audio.play(
    "test.wav"
)
time.sleep(3)