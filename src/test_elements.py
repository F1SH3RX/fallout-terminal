from core.screen import TerminalScreen


screen = TerminalScreen(
    rows=5,
    columns=30
)


screen.add_word(
    "OVERSEER",
    0,
    5
)


print(screen.render())


print("\nELEMENTS:")

for element in screen.elements:
    print(element)