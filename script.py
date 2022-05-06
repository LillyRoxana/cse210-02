import random
## rules
## The player starts the game with 300 points.
## Individual cards are represented as a number from 1 to 13.
## The current card is displayed.
## The player guesses if the next one will be higher or lower.
## The the next card is displayed.
## The player earns 100 points if they guessed correctly.
## The player loses 75 points if they guessed incorrectly.
## If a player reaches 0 points the game is over.
## If a player has more than 0 points they decide if they want to keep playing.
## If a player decides not to play again the game is over.
## 
## requirements
## The program must include a README file.
## The program must include class and method comments.
## The program must have at least two classes.
## The program must remain true to game play described in the overview.
## 
## fun
## Enhanced input validation.
## Enhanced game play and game over messages.
## Enhanced game display, e.g. card suits

# class1 goes here
class Card:
    def __init__(self):
        self.score = 0
        #card value
        self.value = 0
        self.total_score = 0
        self.play = True

    def play(self):
        self.value = random.randint(1, 13)
        self.guess = input("Higher or lower? [h/l]: ")## INPUT ##
        self.prior = self.value
        self.score = 100 if self.guess == "h" and self.value > self.prior or self.guess == "l" and self.value < self.prior
          else self.score = -75
        
        self.total_score += self.score

    def 

# class2 goes here
class Director:
    def start_game(self):
        print("Welcome to Hilo Card Game")
        while self.play == True:
            self.play()
# method goes here

print(self.score)
