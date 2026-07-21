import random


ASCII_CHARS = "!@#$%^&*()_+-={}[]<>?/\\|"


def generate_noise(length):
    return "".join(
        random.choice(ASCII_CHARS)
        for _ in range(length)
    )