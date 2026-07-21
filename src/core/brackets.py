import random


BRACKET_PAIRS = [
    ("(", ")"),
    ("[", "]"),
    ("{", "}"),
    ("<", ">")
]


def generate_bracket():

    opening, closing = random.choice(
        BRACKET_PAIRS
    )

    noise_length = random.randint(
        2,
        6
    )

    noise = "".join(
        random.choice(
            "!@#$%^&*"
        )
        for _ in range(noise_length)
    )

    return (
        opening +
        noise +
        closing
    )