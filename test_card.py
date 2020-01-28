import unittest
from Card import Card

class TestCard(unittest.TestCase):

    def test_show(self):
        """Tests card displays correct value and suit"""
        print('Test show')
        card = Card(11, 'Spades')
        self.assertEqual(card.show(), 'Jack of Spades')
    
    def test_get_value(self):
        """Tests card has correct value"""
        print('Test Get Value')
        card = Card(12, 'Hearts')
        self.assertEqual(card.get_value(), 12)

if __name__ == '__main__':
    unittest.main()