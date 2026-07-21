from core.hacking import HackingGame
from core.terminal import Terminal
from ui.menu import PasswordMenu


words = [
    "OVERSEER",
    "SECURITY",
    "DIRECTOR",
    "FACILITY"
]


game = HackingGame(
    "OVERSEER",
    words
)


terminal = Terminal(
    game,
    None
)


menu = PasswordMenu(words)


menu.show()


selected = menu.get_selection()


print(
    terminal.attempt(selected)
)