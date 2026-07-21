from core.hacking import HackingGame
from core.screen import TerminalScreen
from core.terminal import Terminal
from core.session import GameSession


game = HackingGame(
    "OVERSEER",
    [
        "OVERSEER",
        "SECURITY",
        "DIRECTOR"
    ]
)


screen = TerminalScreen(
    5,
    40
)


screen.add_word(
    "OVERSEER",
    0,
    10
)


terminal = Terminal(
    game,
    screen
)


session = GameSession(
    terminal
)


print(
    session.completed
)


terminal.click(
    0,
    12
)


session.update()


print(
    session.completed
)