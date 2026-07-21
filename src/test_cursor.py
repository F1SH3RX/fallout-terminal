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

screen.elements.append(
    TerminalElement(
        "DIRECTOR",
        "WORD",
        2,
        15
    )
)

cursor = Cursor(screen)

print(cursor.current())

cursor.next()
print(cursor.current())

cursor.next()
print(cursor.current())

cursor.previous()
print(cursor.current())