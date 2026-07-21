class TerminalRenderer:

    def __init__(self, start_address=0xF420):
        self.start_address = start_address


    def render(self, screen):

        output = []

        for row in range(screen.rows):

            address = hex(
                self.start_address + row * 0x10
            )

            line = screen.get_line(row)

            output.append(
                f"{address.upper()}  {line}"
            )

        return "\n".join(output)