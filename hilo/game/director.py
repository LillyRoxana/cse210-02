from game.card import Card

class Director:
   
    def __init__(self):
        
        self.keep_playing = True
        self.score = 300
        self.dealer = Card()

    
    def start_game(self):
        
       

        while self.keep_playing:
            
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            self.can_deal()

    
    def get_inputs(self):
        print(f"Welcome to Hilo Game!")
        self.dealer.deal_card()
        print(f"\nThe card is: {self.dealer.current_card}")
        self.dealer.get_guess()
        
        self.dealer.deal_next_card()
        print(f"Next card was: {self.dealer.next_card}")



    def do_updates(self):
    
        points = self.dealer.get_points()
        self.score += points
       
      
         
   
    def do_outputs(self):
      
        print(f"Your score is: {self.score}")
        if self.can_deal():
            choice = input("Keep playing? [y/n]: ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False
    
    
    
    
    
    
   
    def can_deal(self):
        
        return self.score > 0

