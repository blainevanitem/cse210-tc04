class Dealer:
    def __init__(self):
        self.cards = []
        self.guess = True


        pass
    def get_points(self):
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
        print(f'your card is {self.cards[0]}')

        guess = input("will it be H/L")
        if guess.capitalize() == "H":
            higher = self.card[0] + 1
            if higher > self.card[0]:
                self.guess = True
            else:
                self.guess = False
        if guess.capitalize() == "L":
            lower = self.card[0] - 1
            if lower > self.card[0]:
                self.guess = True
            else:
                self.guess = False