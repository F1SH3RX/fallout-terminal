from core.screen import TerminalScreen
from core.cursor import Cursor


screen = TerminalScreen(
    16,
    32
)

cursor = Cursor(screen)


print(
    cursor.row,
    cursor.column
)


cursor.move_right()
cursor.move_right()
cursor.move_down()


print(
    cursor.row,
    cursor.column
)


cursor.move_left()
cursor.move_up()


print(
    cursor.row,
    cursor.column
)