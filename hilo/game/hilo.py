import random

# Class:
# Instantiate the class that will do the shuffling of the cards

class Hilo:
    def __init__(self):
        self.value = 0


# Method:
# Return ad random number between 1 and 13.

    def shuffle_card(self):
        self.value = random.randint(1, 13)
        self.suit = random.randint(1, 4)
        if self.suit == 1:
            self.suit = "Spades"
        elif self.suit == 2:
            self.suit = "Clubs"
        elif self.suit == 3:
            self.suit = "Hearts"
        else:
            self.suit = "Diamonts"
        return self.value, self.suit
