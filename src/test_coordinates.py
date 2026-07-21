from core.hacking import HackingGame
from core.screen import TerminalScreen
from core.terminal import Terminal


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


print(
    terminal.get_element_at(0, 12)
)


print(
    terminal.get_element_at(3, 12)
)