import random

class Dealer:
    '''This class will be the person who gives cars and guesses from the player.'''

    def __init__(self):
        self.cards = []
        self.guess = True


        pass
    def get_points(self):
        if self.guess == True:
            return 100
        elif self.guess == False:
            return -75
        
    def deal_cards(self):
        '''This gets 2 random cards from the dealer'''

        if len(self.cards) == 0:
            for card in range(0,2):
                card = random.randint(1,13)
                self.cards.append(card)
        if len(self.cards) == 1:
            card = random.randint(1,13)
            self.cards.append(card)

    def get_guess(self):
        '''Gets the guess from the player of if the next card will be higher or lower.'''

        print(f'Your card is {self.cards[0]}')

        guess = input("Will it be H/L?")
        if self.cards[0] < self.cards[1] and guess.capitalize() == "H" or self.cards[0] > self.cards[1] and guess.capitalize() == "L":
            self.guess = True
        else:
            self.guess = False
        self.cards.pop(0)
