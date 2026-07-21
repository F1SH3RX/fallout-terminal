class HackingGame:

    def __init__(self, password, words):
        self.password = password  #the correct password
        self.words = words   #all words in the game
        self.attempts = 4   #number of attempts allowed
        self.finished = False  #whether the game is finished

    def calculate_likeness(self, guess):
        correct = 0

        for a, b in zip(self.password, guess):
            if a == b:
                correct += 1

        return correct
    
    def guess(self, word):

        if self.finished:
            return "Terminal locked"

        if word == self.password:
            self.finished = True
            return "ACCESS GRANTED"

        self.attempts -= 1

        likeness = self.calculate_likeness(word)

        if self.attempts == 0:
            self.finished = True
            return "ACCESS DENIED - LOCKED"

        return f"{likeness}/{len(self.password)} correct"