import random

class Card:
   

    def __init__(self):
        
        self.current_card = []
        self.next_card = []
        self.guess = []
        
       
        
    def deal_card(self):
        
        self.current_card.clear()
        result = random.randint(1,13)
        self.current_card.append(result)
        
    def get_guess(self):
        
        self.guess.clear()
        guess = input("Higher or lower? [h/l]: ")
        self.guess.append(guess)  
        
    
    
    def deal_next_card(self):
        
        self.next_card.clear()
        next_result = random.randint(1,13)
        self.next_card.append(next_result)
        
    
    
    def get_points(self):
       
        guess = self.guess
        score = 0
        if guess == "h":
            if self.next_card > self.current_card:
                score = 100
            if self.next_card < self.current_card:
                score = -75
        elif guess == "l":
            if self.next_card < self.current_card:
                score = 100
            if self.next_card > self.current_card:
                score = -75
        return score        




