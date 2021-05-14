class Dealer:
    def __init__(self):
        self.cards = []
        self.guess = ""


        pass
    def get_points(self):
        if self.cards[0] > self.cards[1] and self.guess == "H":
            return 100
        elif self.cards[0] < self.cards[1] and self.guess == "L":
            return 100
        else:
            return -75 
        '''
        If True +100 points
        If False - 75 points
        return points
        '''
    def deal_cards(self):
        '''
        get 2 cards 
        '''
        pass
    def get_guess(self):
        '''
        display card
        self.guess = input
        '''
        pass