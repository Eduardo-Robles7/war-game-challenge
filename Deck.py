from Card import Card
from Player import Player
import random

class Deck:
    def __init__(self):
        """Initialize values and suits"""
        self.cards = []
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        #self.initialize_deck()

    def initialize_deck(self):
        """Initializes deck with every card"""
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(value, suit))
    
    def show_deck(self):
        """Displays are cards in the deck"""
        if self.cards:
            for card in self.cards:
                card.show()
            return 1
        else:
            return -1


    def shuffle_deck(self):
        """Shuffles the deck of cards"""
        random.shuffle(self.cards)

    def split_deck(self, player_one, player_two):
        """Splits deck of cards between two players"""
        player_one.add_cards(self.cards[:len(self.cards) // 2])
        player_two.add_cards(self.cards[len(self.cards) // 2:])