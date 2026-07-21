from core.bracket import BracketAction
from core.cursor import Cursor
class Terminal:

    def __init__(
        self,
        game,
        screen
    ):
        self.game = game
        self.screen = screen
        self.cursor = Cursor(screen)
        self.bracket_action = BracketAction(self)

    def move_cursor_next(self):

        self.cursor.next()


    def move_cursor_previous(self):

        self.cursor.previous()


    def select_current(self):

        element = self.cursor.current()

        if element is None:
            return "NOTHING SELECTED"

        return self.select_element(element)

    def select_element(self, element):

        if element.element_type == "WORD":

            result = self.game.guess(
                element.value
            )
            return result

        if element.element_type == "BRACKET":

            return self.bracket_action.activate(element)

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
                self.screen.hide_element(element)
                return
            
    def get_element_at(self, row, column):

        for element in self.screen.elements:

            if not element.active:
                continue

            if element.row != row:
                continue

            start = element.column
            end = element.column + len(element.value)

            if start <= column < end:
                return element

        return None
    
    def click(self, row, column):

        element = self.get_element_at(
            row,
            column
        )

        if element is None:
            return "NOTHING SELECTED"

        return self.select_element(element)
    def select_cursor(self):

        element = self.get_element_at(
            self.cursor.row,
            self.cursor.column
        )

        if element is None:
            return "NOTHING SELECTED"

        return self.select_element(element)