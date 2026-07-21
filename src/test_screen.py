from core.screen_generator import ScreenGenerator
from ui.renderer import TerminalRenderer
words = [
    "OVERSEER",
    "SECURITY",
    "DIRECTOR"
]


generator = ScreenGenerator()


screen = generator.generate(words)


renderer = TerminalRenderer()
print(
    renderer.render(screen)
)
print("\nELEMENTS:")

for element in screen.elements:
    print(element)