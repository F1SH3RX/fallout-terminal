from core.screen import TerminalScreen
from core.cursor import Cursor
from ui.renderer import TerminalRenderer


screen = TerminalScreen(
    4,
    32
)


screen.grid[0] = list(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456"
)


cursor = Cursor(screen)

cursor.column = 5


renderer = TerminalRenderer()


print(
    renderer.render(
        screen,
        cursor
    )
)