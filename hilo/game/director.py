from game.card import Card

class Director:

    def __init__(self):
        self.card = []
        self.is_playing = True
        self.score = 300
        self.total_score = 0

    def start_game(self):
        print("Welcome to Hilo Card Game")
        while self.is_playing:
            self.get_inputs()
            self.get_guess()            
            self.do_updates()
            self.do_outputs()
    
    def get_inputs(self):
        play_card = input("Play again? y/n")
        self.is_playing = (play_card == "y")

    def get_guess(self):
        guess_card = input("Higher or lower? h/l")
        self.is_playing = (guess_card == "h" or guess_card == "l")

    def do_updates(self):
        if not self.is_playing: 
            return

    def do_outputs(self):
        if not self.is_playing: 
            return

