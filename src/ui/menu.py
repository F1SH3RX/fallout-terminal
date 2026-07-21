class PasswordMenu:

    def __init__(self, words):
        self.words = words


    def show(self):

        print("\nSELECT PASSWORD:\n")

        for index, word in enumerate(self.words):

            print(
                f"{index + 1}) {word}"
            )


    def get_selection(self):

        choice = int(
            input("\n> ")
        )

        return self.words[choice - 1]