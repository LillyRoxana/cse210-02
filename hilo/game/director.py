from ast import Break, Try
from game.hilo import Hilo

class Director:
    
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """
    def __init__(self):

        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = Hilo()
        self.is_playing = True
        self.score = 300
        self.total_score = 0


# Method:
# Start the game here. Use while loop to help the game continue. Game will until
# player reaches 0 points, or until player selects "n" at the prompt.

    def start_game(self):        
        print("Welcome to Hilo Card Game")
        while self.is_playing:
            self.card2 = self.card.shuffle_card()
            print(f"\nThe card is: {self.card2[0]} of {self.card2[1]}")
            self.get_inputs()
            self.update()


# Method:
# The player needs to get if the next card will be higher or lower. If they choose
# correctly, they get 100 points. If they choose incorrectly, they lose 75 points.

    def get_inputs(self):
        prior = self.card2[0]
        choice = input("Higher or lower? [h/l]: ")  
        self.card2 = self.card.shuffle_card()
        if choice == "h" and self.card2[0] > prior:
            self.total_score = self.score + 100
            self.score = self.total_score
            print(f"Next card was: {self.card2[0]} of {self.card2[1]}")
        elif choice == "l" and self.card2[0] < prior:
            self.total_score = self.score + 100
            self.score = self.total_score
            print(f"Next card was: {self.card2[0]} of {self.card2[1]}")
        elif choice == "h" and self.card2[0] < prior:
            self.total_score = self.score - 75
            self.score = self.total_score
            print(f"Next card was: {self.card2[0]} of {self.card2[1]}")
        elif choice == "l" and self.card2[0] > prior:
            self.total_score = self.score - 75
            self.score = self.total_score
            print(f"Next card was: {self.card2[0]} of {self.card2[1]}")
        else:
            print("That was not a valid option")
            self.get_inputs()
        

# Method:
# Check to see if the score is less than or equal to zero. Also inquire if the
# player wants to continue playing.

    def update(self):
        if self.total_score <= 0:
            print(f"Your score is: {self.total_score}")
            print("GAME OVER!!!")
            self.is_playing = False
        else:
            print(f"Your score is: {self.total_score}")
            play_card = input("Play again? [y/n] ")
            if play_card == "y":
                self.is_playing = True
            elif play_card == "n":
                print("Thank you for playing!!!")
                self.is_playing = False
            else:
                print("That was not a valid option")
                self.update()


