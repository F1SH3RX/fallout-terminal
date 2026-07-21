from core.bracket import BracketAction
class Terminal:

    def __init__(
        self,
        game,
        screen
    ):
        self.game = game
        self.screen = screen
        self.bracket_action = BracketAction(self.game)

    def select_element(self, element):

        if element.element_type == "WORD":

            return self.game.guess(
                element.value
            )


        if element.element_type == "BRACKET":

            return self.bracket_action.activate()

    def attempt(self, word):

        result = self.game.guess(word)

        return result
    
    def remove_word_element(self, word):

        for element in self.screen.elements:

            if (
                element.value == word
                and element.element_type == "WORD"
            ):
                element.active = False
                return