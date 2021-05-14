from game.Dealer import Dealer

class Director:
    def __init__(self,):
        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()
    def start_game(self):
        while self.keep_playing == True:
            self.get_inputs()
            self.do_points()
            self.display_outputs()
    def get_inputs(self):
        self.dealer.deal_cards()
        self.dealer.get_guess()
    def do_points(self):
        points = self.dealer.get_points()
        self.score += points
    def display_outputs(self):
            print(f"the card is {self.dealer.cards[0]}")
            print(f"your points are {self.score}")
            self.can_play()
    
    #Determines if the score is 0 and the play is over, or if the player wants to continue play or not.
    def can_play(self):
        if(self.score <= 0):
            self.keep_playing = False
        else:
            self.answer = input(print("Would you like to keep playing? [Yes/No]"))
            if(self.answer == "Yes" or self.answer == "yes"):
                self.keep_playing = True
            else:
                self.keep_playing = False
