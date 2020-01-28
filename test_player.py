import unittest
from Card import Card
from Player import Player

class TestPlayer(unittest.TestCase):
    
    def test_show_hand(self):
        """Tests player has a hand"""
        print('Test Show Hand')
        player = Player('Bob')
        self.assertEqual(player.show_hand(), -1)
    
    def test_add_card(self):
        """Tests player can add a new card"""
        print('Test Add Card')
        player = Player('Bob')
        card = Card(9, 'Spades')
        player.add_card(card)
        self.assertEqual(len(player.hand), 1)
    
    def test_add_cards(self):
        """Tests player can add multiple new cards"""
        print('Test Add Cards')
        player = Player('Bob')
        cards = [Card(2, 'Clubs'), Card(9, 'Hearts'), Card(5, 'Spades')]
        player.add_cards(cards)
        self.assertEqual(len(player.hand), 3)
    
    def test_pop_card(self):
        """Tests player draws top card from hand"""
        print('Test Pop Card')
        player = Player('Bob')
        card = Card(9, 'Spades')
        player.add_card(card)
        res_card = player.pop_card()
        self.assertEqual(res_card.value, card.value)
        self.assertEqual(res_card.suit, card.suit)

    def test_reset_hand(self):
        """Tests player hand is reset to zero cards"""
        print('Test Reset Hand')
        player = Player('Bob')
        card = Card(9,'Spades')
        player.add_card(card)
        player.reset_hand()
        self.assertEqual(len(player.hand), 0)
    
    def test_has_cards(self):
        """Tests if player has cards in hand"""
        print('Test Has Cards')
        player = Player('Bob')
        card = Card(9, 'Spades')
        player.add_card(card)
        self.assertEqual(player.has_cards(), True)
    
    def test_card_count(self):
        """Tests player hand count"""
        print('Test Card Count')
        player = Player('Bob')
        card = Card(9, 'Spades')
        player.add_card(card)
        self.assertEqual(player.card_count(), 1)

if __name__ == '__main__':
    unittest.main()