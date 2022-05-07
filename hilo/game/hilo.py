import random

class Hilo:
    def __init__(self):
        self.score = 0
        self.value = 0
        self.total_score = 0
        self.play = True

    def play(self):
        self.value = random.randint(1, 13)
        self.guess = input("Higher or lower? [h/l]: ")## INPUT ##
        self.prior = self.value
        if (self.guess == "h" and self.value > self.prior) or (self.guess == "l" and self.value < self.prior):
            self.score = 100
        else:
            self.score = -75

        self.total_score += self.score

