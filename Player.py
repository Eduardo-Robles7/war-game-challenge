from Card import Card
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def show_hand(self):
        for card in hand:
            card.show()

    def add_card(self, card):
        self.hand.append(card)
    
    def add_cards(self, cards):
        self.hand.extend(cards)

    def discard_card(self):
        return self.hand.pop()
