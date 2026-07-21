from core.hacking import HackingGame


game = HackingGame(
    "OVERSEER",
    [
        "OVERSEER",
        "OVERTIME",
        "SECURITY",
        "DIRECTOR"
    ]
)


print(game.guess("OVERTIME"))

print(game.guess("SECURITY"))

print(game.guess("OVERSEER"))