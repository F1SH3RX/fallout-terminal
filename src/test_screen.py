from core.screen import TerminalScreen


screen = TerminalScreen(
    rows=5,
    columns=20
)


screen.set_character(0,0,"R")
screen.set_character(0,1,"O")
screen.set_character(0,2,"B")
screen.set_character(0,3,"C")


print(screen.render())