from game.hilo import Hilo

class Director:

     def __init__(self):
        self.hilo = []
        self.is_playing = True
        self.score = 300
        self.total_score = 0
        self.guess = ""
        self.hilo = Hilo()

     def start_game(self):
        
        print("Welcome to Hilo Card Game!")
        while self.is_playing:
            self.get_inputs()
            self.get_guess()
            self.do_updates()
            self.do_outputs()
    
     def get_inputs(self):
        play_card = input("Play again? [y/n]: ")
        self.is_playing = (play_card == "y")

     def get_guess(self):
        guess = input("Higher or lower? [h/l]: ")
        self.is_playing = (guess == "h" or guess == "l")

     def do_updates(self):
        if not self.is_playing: 
            return

        value = ""
        value = "this is a test"
        print(value)
        if self.guess == "h":
            print(f"You guessed that the card would be higher.")
        elif self.guess == "l":
            print(f"You guess that the card would be lower.")
        else:
            print(f"You done messed up.")

     def do_outputs(self):
        if not self.is_playing: 
            return