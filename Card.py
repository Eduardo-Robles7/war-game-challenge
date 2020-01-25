class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def show(self):
        switcher = {
            11:'Jack',
            12:'Queen',
            13:'King',
            14:'Ace'
        }
        val = switcher.get(self.value, self.value)
        print("{} of {}".format(val, self.suit))