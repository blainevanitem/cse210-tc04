import random

class Dealer:
    def __init__(self):
        self.cards = []
        self.guess = True


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
        print(f'your card is {self.cards[0]}')

        guess = input("will it be H/L")
        if guess.capitalize() == "H":
            higher = self.cards[0] + 1
            if higher > self.cards[0]:
                self.guess = True
            else:
                self.guess = False
        if guess.capitalize() == "L":
            lower = self.cards[0] - 1
            if lower > self.cards[0]:
                self.guess = True
            else:
                self.guess = False
        self.cards.pop(0)
