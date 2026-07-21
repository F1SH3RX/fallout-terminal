class HackingGame:

    def __init__(self, password, words):
        self.password = password  #the correct password
        self.words = words   #all words in the game
        self.attempts = 4   #number of attempts allowed
        self.locked = False  #true if the game is locked, false otherwise
        self.success = False  #true if the game is won, false otherwise

    def calculate_likeness(self, guess):
        correct = 0

        for a, b in zip(self.password, guess):
            if a == b:
                correct += 1

        return correct
    
    def guess(self, word):

        if self.locked:
            return "TERMINAL LOCKED"
        
        if self.success:
            return "ACCESS ALREADY GRANTED"

        if word not in self.words:
            return "INVALID SELECTION"

        if word == self.password:
            self.success = True
            return "ACCESS GRANTED"

        self.attempts -= 1

        likeness = self.calculate_likeness(word)

        if self.attempts == 0:
            self.locked = True
            return "ACCESS DENIED - LOCKED"

        return f"{likeness}/{len(self.password)} correct\n" 