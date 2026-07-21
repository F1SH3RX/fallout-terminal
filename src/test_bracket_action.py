from core.hacking import HackingGame
from core.bracket import BracketAction


game = HackingGame(
    "OVERSEER",
    [
        "OVERSEER",
        "SECURITY",
        "DIRECTOR",
        "FACILITY"
    ]
)


game.attempts = 2


action = BracketAction(game)


print(action.activate())

print(
    "Attempts:",
    game.attempts
)

print(
    "Words:",
    game.words
)