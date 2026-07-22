class MainMenu:

    def __init__(self, audio=None):

        self.audio = audio
        self.options = [
            "ACCESS SECURITY SYSTEM",
            "SYSTEM INFORMATION",
            "USER LOGS",
            "SECURITY DATABASE",
            "NETWORK STATUS",
            "SHUTDOWN"
        ]

        self.selected = 0

    def play_move_sound(self):

        if self.audio:

            self.audio.play(
                "cursor.wav"
            )
            
    def move_up(self):

        self.selected -= 1

        if self.selected < 0:
            self.selected = len(self.options) - 1
        self.play_move_sound()

    def move_down(self):

        self.selected += 1

        if self.selected >= len(self.options):
            self.selected = 0
        self.play_move_sound()

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
            "CPU: Z80 COMPATIBLE"
        ]


    def get_logs(self):

        return [
            "USER LOGS",
            "",
            "[07/03/2077]",
            "Routine maintenance completed.",
            "",
            "[11/06/2077]",
            "Unauthorized login detected.",
            "",
            "[18/08/2077]",
            "Vault security lockdown enabled."
        ]


    def get_security_database(self):

        return [
            "SECURITY DATABASE",
            "",
            "ACCESS LEVEL: 4",
            "FIREWALL: ACTIVE",
            "INTRUSION DETECTION: ONLINE",
            "ENCRYPTION: AES-256",
            "",
            "STATUS: SECURE"
        ]


    def get_network_status(self):

        return [
            "NETWORK STATUS",
            "",
            "ROBCO MAINFRAME: ONLINE",
            "PRIMARY NODE: CONNECTED",
            "BACKUP NODE: ONLINE",
            "",
            "LATENCY: 12 ms",
            "PACKET LOSS: 0%"
        ]