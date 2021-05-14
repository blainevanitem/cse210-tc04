class Director:
    def __init__(self,):
        self.keep_playing = True
        self.score = 300
        self.dealer = game.Dealer()
    def start_game(self):
        while self.keep_playing == True:
            self.get_inputs()
            self.do_points()
            self.display_outputs()
    def get_inputs(self):
        self.dealer.deal_card()
        self.dealer.get_guess()
    def do_points(self):
        points = self.dealer.get_points()
        self.score += points
    def display_outputs(self):

        pass
    def can_play(self):
            
        '''
        If score bad   
            keep_playing = False
        else
            whant to play = input
            if yes
                self.keep playing = True
            else
                self.keep playing = False
        '''    