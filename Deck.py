from Card import Card
import random
class Deck:
    def __init__(self):
        self.cards = []
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def initialize_deck(self):
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(value, suit))
    
    def show_deck(self):
        start = 1
        for card in self.cards:
            card.show()

    def shuffle_deck(self):
        random.shuffle(self.cards)


deck = Deck()
deck.initialize_deck()
deck.shuffle_deck()
deck.show_deck()