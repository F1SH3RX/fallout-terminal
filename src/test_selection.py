from core.hacking import HackingGame
from core.terminal import Terminal
from core.elements import TerminalElement


game = HackingGame(
    "OVERSEER",
    [
        "OVERSEER",
        "SECURITY",
        "DIRECTOR",
        "FACILITY"
    ]
)


terminal = Terminal(
    game,
    None
)


word = TerminalElement(
    "SECURITY",
    "WORD",
    0,
    0
)


bracket = TerminalElement(
    "[!@#]",
    "BRACKET",
    1,
    0
)


print(
    terminal.select_element(word)
)


print(
    terminal.select_element(bracket)
)