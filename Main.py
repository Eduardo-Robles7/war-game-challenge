from Deck import Deck
from Player import Player

def main():    
    #setup players
    player_one = Player('Eduardo')
    player_two = Player('CPU')

    #setup deck and divide cards
    deck = Deck()
    deck.shuffle_deck()
    deck.show_deck()

if __name__ == '__main__':
    main()