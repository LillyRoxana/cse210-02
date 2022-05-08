from shuffle import Hilo

## Rules
## - The player starts the game with 300 points.
## - Individual cards are represented as a number from 1 to 13.
## - The current card is displayed.
## - The player guesses if the next one will be higher or lower.
## - The the next card is displayed.
## - The player earns 100 points if they guessed correctly.
## - The player loses 75 points if they guessed incorrectly.
## - If a player reaches 0 points the game is over.
## - If a player has more than 0 points they decide if they want to keep playing.
## - If a player decides not to play again the game is over.
## 
## Requirements
## - The program must include a README file.
## - The program must include class and method comments.
## - The program must have at least two classes.
## - The program must remain true to game play described in the overview.
## 
## Things to do for fun:
## - Enhanced input validation.
## - Enhanced game play and game over messages.
## - Enhanced game display, e.g. card suits

class Director:
    """A person who directs the game. 
        
        The responsibility of a Director is to control the sequence of play.

        Attributes:
            card (Hilo): A number between 1 to 13.
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

#*This method start the game. Have a while loop that help us to continue the game, 
#*until the player reach 0 or less, or until the player inputs "n"
    def start_game(self):
        print("Welcome to Hilo Card Game")
        while self.is_playing:
            self.card2 = self.card.shuffle_card()
            print(f"The card is: {self.card2}")
            self.get_inputs()  
            self.update()       

#*Method where the player need to guess if the card is higher or lower. If he choose right gets 100 points, if not -75 points. 
    def get_inputs(self):
        prior = self.card2
        choice = input("Higher or lower? [h/l] ")
        self.card2 = self.card.shuffle_card()
        print(f"Next card was: {self.card2}")
        if choice == "h" and self.card2 > prior:
            self.total_score = self.score + 100
            self.score = self.total_score
        elif choice == "l" and self.card2 < prior:
            self.total_score = self.score + 100
            self.score = self.total_score
        elif choice == "h" and self.card2 < prior:
            self.total_score = self.score - 75
            self.score = self.total_score
        elif choice == "l" and self.card2 > prior:
            self.total_score = self.score - 75
            self.score = self.total_score
        else:
            print("That was not a valid option")
            self.get_inputs()

#*Method to check the total score. And where the player decide if he wants to continue. 
    def update(self):
        if self.total_score <= 0:
            print(f"Your score is: {self.total_score}")
            print("GAME OVER!!!")
            self.is_playing = False
        else:
            print(f"Your score is: {self.total_score}")
            play_card = input("Play again? y/n\n")
            if play_card == "y":
                self.is_playing = True
            elif play_card == "n":
                print("Thank you for playing!!!")
                self.is_playing = False
            else:
                print("That was not a valid option")
                self.update()

