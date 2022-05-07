import random

class Card:
    """The responsability of Card is drawing the cards, keeps track
    of the previous card, and determines if the drawn card is hi or lo.
    Attributes:
        
        guess: a instant of Card
        current_card: a random card drawn from the deck
        next_card: the previous card, used to evaluate hi/lo
    """
   
   

    def __init__(self):
        
        """Constructs a new instance of Card.
        Args:
            self (Card): An instance of Card.
        """
        self.current_card = []
        self.next_card = []
        self.guess = []
        
       
        
    def deal_card(self):
        """Generates a new random value and calculates the result for the Card.
        
        Args:
            self (Card): An instance of Card.
        """
        self.current_card.clear()
        result = random.randint(1,13)
        self.current_card.append(result)
        
    def get_guess(self):
        
        self.guess.clear()
        guess = input("Higher or lower? [h/l]: ")
        self.guess.append(guess)  
        
    
    
    def deal_next_card(self):
        """Generates a new random value and calculates the result for the next Card.
        
        Args:
            self (Card): An instance of Card.
        """
        self.next_card.clear()
        next_result = random.randint(1,13)
        self.next_card.append(next_result)
        
    
    
    def get_points(self):
        
        """ Determines if the drawn (current) card is higher or lower than
        the previous card.
        Args:
            self (Card): An instance of the Card class.
        Returns:
            str: if higher, returns 'hi'
                 if lower, returns 'lo'
                 if equal, returns 'equal'
        """
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




