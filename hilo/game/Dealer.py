import random

class Dealer:
    def __init__(self):
        self.cards = []
        self.guess = ""


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
        if len(self.cards) == 0:
            for card in range(0,2):
                card = random.randint(1,13)
                self.cards.append(card)
        if len(self.cards) == 1:
            card = random.randint(1,13)
            self.cards.append(card)

    def get_guess(self):
        '''
        display card
        self.guess = input
        '''
        
        pass