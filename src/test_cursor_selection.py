from core.screen import TerminalScreen
from core.elements import TerminalElement
from core.terminal import Terminal
from core.hacking import HackingGame


screen = TerminalScreen(
    5,
    20
)


element = TerminalElement(
    "OVERSEER",
    "WORD",
    0,
    5
)


screen.elements.append(element)


game = HackingGame(
    "OVERSEER",
    ["OVERSEER"]
)


terminal = Terminal(
    game,
    screen
)


terminal.cursor.row = 0
terminal.cursor.column = 6


print(
    terminal.select_cursor()
)