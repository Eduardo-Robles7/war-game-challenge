class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __eq__(self, other_card):
        return self.value == other_card.value
    
    def __lt__(self, other_card):
        return self.value < other_card.value
    
    def __gt__(self, other_card):
        return self.value > other_card.value
    
    def show(self):
        switcher = {
            11:'Jack',
            12:'Queen',
            13:'King',
            14:'Ace'
        }
        val = switcher.get(self.value, self.value)
        return "{} of {}".format(val, self.suit)
    
    def get_value(self):
        return self.value