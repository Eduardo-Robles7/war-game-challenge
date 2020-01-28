import unittest
from Deck import Deck
from Card import Card
from Player import Player
class TestDeck(unittest.TestCase):

    def test_initialize_deck(self):
        """Tests the initialization of deck with proper cards"""
        print('Test Initialize Deck')
        deck = Deck()
        deck.initialize_deck()
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        cards = []
        for suit in suits:
            for value in values:
                cards.append(Card(value, suit))
        self.assertEqual(len(deck.cards), len(cards))
    
    def test_show_deck(self):
        """Tests deck showing cards if count is greater than zero"""
        print('Test Show Deck')
        deck = Deck()
        self.assertEqual(deck.show_deck(), -1)
        deck.initialize_deck()
        self.assertEqual(deck.show_deck(), 1)

    def test_shuffle_deck(self):
        """Tests the shuffling of cards in the deck"""
        print('Test Shuffle Deck')
        deck = Deck()
        deck2 = Deck()
        deck.initialize_deck()
        deck2.initialize_deck()
        deck.shuffle_deck()
        equal = False
        for card in deck.cards:
            for card2 in deck2.cards:
                if card.value == card2.value:
                    equal == True
        self.assertEqual(equal, False)

    def test_split_deck(self):
        """Tests splitting the deck of cards between two players"""
        print('Test Split Deck')
        deck = Deck()
        player1 = Player('Bob')
        player2 = Player('Sam')
        deck.split_deck(player1, player2)
        self.assertEqual(len(player1.hand), len(player2.hand))


if __name__ == '__main__':
    unittest.main()