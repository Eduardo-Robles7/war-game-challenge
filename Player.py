from Card import Card

class Player:
    def __init__(self, name):
        """Initialize name and hand"""
        self.name = name
        self.hand = []

    def show_hand(self):
        """Displays all cards in player hand"""
        if self.hand:
            for card in self.hand:
                card.show()
                return 1
        else:
            return -1

    def add_card(self, card):
        """Adds a card to player hand"""
        if card:
            self.hand.append(card)
    
    def add_cards(self, cards):
        """Adds a list of cards to player hand"""
        if cards:
            self.hand.extend(cards)

    def pop_card(self):
        """Returns top card hand"""
        return self.hand.pop()

    def reset_hand(self):
        """Resets hand to be empty"""
        self.hand = []
    
    def has_cards(self):
        """Returns true if player has cards, false otherwise"""
        if len(self.hand) > 0:
            return True
        else:
            return False

    def card_count(self):
        """Returns count of cards in hand"""
        return len(self.hand)