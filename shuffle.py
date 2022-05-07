import random
#Hilo Class help us to shuffle the cards, between 1 and 13. 
class Hilo:
    def __init__(self):
        self.value = 0

#*This method returns a random number between 1 and 13. 
    def shuffle_card(self):
        self.value = random.randint(1, 13)
        return self.value