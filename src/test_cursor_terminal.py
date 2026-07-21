from core.screen import TerminalScreen
from core.cursor import Cursor
from core.elements import TerminalElement

screen = TerminalScreen(5, 20)

screen.elements.append(
    TerminalElement(
        "OVERSEER",
        "WORD",
        0,
        5
    )
)

screen.elements.append(
    TerminalElement(
        "SECURITY",
        "WORD",
        1,
        10
    )
)

cursor = Cursor(screen)

print("Selected:", cursor.current().value)

cursor.next()

print("Selected:", cursor.current().value)