from game.Dealer import Dealer

class Director:
    '''This class will control the gameplay in the correct order'''

    def __init__(self):
        '''Initializing attributes that we will need in the program.'''

        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()

    def start_game(self):
        '''Keeps a loop going until the program returns keep_playing as False'''

        while self.keep_playing == True:
            self.get_inputs()
            self.do_points()
            self.display_outputs()

    def get_inputs(self):
        '''Will call the Dealer to get cards and the players guess'''

        self.dealer.deal_cards()
        self.dealer.get_guess()

    def do_points(self):
        '''Will calculate the point that will be added to the initial score.'''

        points = self.dealer.get_points()
        self.score += points

    def display_outputs(self):
        '''Displays on the screen what the card is and the score.'''

        print(f"The card is {self.dealer.cards[0]}")
        print(f"Your points are {self.score}")
        self.can_play()

    def can_play(self):
        '''Determines if the score is 0 and the play is over, or if the player wants to continue play or not.'''

        if(self.score <= 0):
            self.keep_playing = False
        else:
            self.answer = input("Would you like to keep playing? [Yes/No]")
            if(self.answer == "Yes" or self.answer == "yes"):
                self.keep_playing = True
            else:
                self.keep_playing = False
