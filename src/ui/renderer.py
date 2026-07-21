class TerminalRenderer:

    def __init__(self):
        self.width = 16


    def render(self, words):

        for index, word in enumerate(words):
            address = hex(0xF420 + index * 0x10)

            print(
                f"{address}  {word}"
            )