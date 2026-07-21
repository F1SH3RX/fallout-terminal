from core.hacking import HackingGame
from core.screen_generator import ScreenGenerator
from core.terminal import Terminal
from ui.renderer import TerminalRenderer

password = "OVERSEER"

words = [
    "OVERSEER",
    "SECURITY",
    "DIRECTOR",
    "FACILITY",
]


game = HackingGame(
    password,
    words
)


generator = ScreenGenerator()

screen = generator.generate(words)


terminal = Terminal(
    game,
    screen
)


renderer = TerminalRenderer()

print(
    renderer.render(screen)
)


print()


print(
    terminal.attempt("SECURITY")
)