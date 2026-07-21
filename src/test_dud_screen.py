from core.hacking import HackingGame
from core.screen import TerminalScreen
from core.terminal import Terminal
from ui.renderer import TerminalRenderer


game = HackingGame(
    "OVERSEER",
    [
        "OVERSEER",
        "SECURITY",
        "DIRECTOR",
        "FACILITY"
    ]
)


screen = TerminalScreen(
    5,
    40
)


screen.add_word(
    "FACILITY",
    0,
    5
)


terminal = Terminal(
    game,
    screen
)


renderer = TerminalRenderer()


print("BEFORE:\n")

print(
    renderer.render(screen)
)


terminal.remove_word_element(
    "FACILITY"
)


print("\nAFTER:\n")

print(
    renderer.render(screen)
)