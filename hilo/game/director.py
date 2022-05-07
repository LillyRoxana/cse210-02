from game.card import Card
  

class Director:
          
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        dealer (int): The score for the entire game.
    """
   
    def __init__(self):
      
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.dealer = Card()

    
    def start_game(self):
        
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
       
        while self.keep_playing:
            
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            self.can_deal()

    
    def get_inputs(self):
        
        """Ask the user if they want to roll.
        Args:
            self (Director): An instance of Director.
        """
        print(f"Welcome to Hilo Game!")
        self.dealer.deal_card()
        print(f"\nThe card is: {self.dealer.current_card}")
        self.dealer.get_guess()
        
        self.dealer.deal_next_card()
        print(f"Next card was: {self.dealer.next_card}")



    def do_updates(self):
        
        """Updates the player's score.
        Args:
            self (Director): An instance of Director.
        """
        points = self.dealer.get_points()
        self.score += points
       
      
         
   
    def do_outputs(self):
        """Displays the Hilo and the score. Also asks the player if they want to roll again. 
        Args:
            self (Director): An instance of Director.
        """
        print(f"Your score is: {self.score}")
        if self.can_deal():
            choice = input("Keep playing? [y/n]: ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False
    
    
  
    def can_deal(self):
        
        return self.score > 0
