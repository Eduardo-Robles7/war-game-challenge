from Card import Card
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def show_hand(self):
        for card in self.hand:
            card.show()

    def add_card(self, card):
        self.hand.append(card)
    
    def add_cards(self, cards):
        self.hand.extend(cards)

    def pop_card(self):
        return self.hand.pop()

    def reset_hand(self):
        self.hand = []
    
    def has_cards(self):
        if len(self.hand) > 0:
            return True
        else:
            return False