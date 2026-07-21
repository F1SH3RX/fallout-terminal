class Cursor:

    def __init__(self, screen):

        self.screen = screen

        self.row = 0
        self.column = 0

    def clamp(self):
        if self.row < 0:
            self.row = 0

        if self.row >= self.screen.rows:
            self.row = self.screen.rows - 1

        if self.column < 0:
            self.column = 0

        if self.column >= self.screen.columns:
            self.column = self.screen.columns - 1


    def move_left(self):

        elements = sorted(
            self.elements,
            key=lambda e: (e.row, e.column)
        )

        current = self.current()

        if current is None:
            self.move_to(elements[0])
            return

        index = elements.index(current)

        if index > 0:
            self.move_to(
                elements[index - 1]
            )


    def move_right(self):

        elements = sorted(
            self.elements,
            key=lambda e: (e.row, e.column)
        )

        current = self.current()

        if current is None:
            self.move_to(elements[0])
            return

        index = elements.index(current)

        if index < len(elements) - 1:
            self.move_to(
                elements[index + 1]
            )

    def move_up(self):

        element = self.closest_vertical(
            "up"
        )

        if element:
            self.move_to(element)



    def move_down(self):

        element = self.closest_vertical(
            "down"
        )

        if element:
            self.move_to(element)



    @property
    def elements(self): 

        return [
            element
            for element in self.screen.elements
            if element.active
        ]
    
    def move_to(self, element):

        self.row = element.row
        self.column = element.column

    def current(self):

        for element in self.elements:

            if (
                element.row == self.row
                and element.column == self.column
            ):
                return element

        return None
    
    def closest_vertical(self, direction):

        candidates = []

        for element in self.elements:

            if direction == "up":

                if element.row < self.row:
                    candidates.append(element)

            if direction == "down":

                if element.row > self.row:
                    candidates.append(element)


        if not candidates:
            return None


        return min(
            candidates,
            key=lambda e: (
                abs(e.row - self.row)
                +
                abs(e.column - self.column)
            )
        )