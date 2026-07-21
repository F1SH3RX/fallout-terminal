class MainMenu:

    def __init__(self):

        self.options = [
            "ACCESS SECURITY SYSTEM",
            "SYSTEM INFORMATION",
            "SHUTDOWN"
        ]

        self.selected = 0


    def move_up(self):

        self.selected -= 1

        if self.selected < 0:
            self.selected = len(self.options) - 1



    def move_down(self):

        self.selected += 1

        if self.selected >= len(self.options):
            self.selected = 0



    def current(self):

        return self.options[self.selected]
    
    def get_information(self):

        return [
        "ROBCO INDUSTRIES (TM)",
        "",
        "UNIFIED OPERATING SYSTEM",
        "VERSION 1.0",
        "",
        "TERMINAL STATUS: ONLINE",
        "SECURITY MODULE: ACTIVE",
        "NETWORK LINK: CONNECTED",
        "",
        "MEMORY: 64KB",
        "CPU: Z80 COMPATIBLE",
        "",
        "RETURN TO MAIN MENU"
        ]