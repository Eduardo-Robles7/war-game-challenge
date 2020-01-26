from Card import Card
from Deck import Deck
from Player import Player

def main():    
    #setup players
    player = Player('Eduardo')
    cpu = Player('CPU')

    #setup deck and stashes
    deck = Deck()
    deck.shuffle_deck()
    deck.split_deck(player, cpu)
    player_stash = []
    cpu_stash = [] 
    rounds = 0 

     #run until a player runs out of cards
    while player.has_cards() and cpu.has_cards():
        player_card = player.pop_card()
        cpu_card = cpu.pop_card()
        
        #display cards
        print('{}: {}\n'.format(player.name, player_card.show()))
        print('{}: {}\n'.format(cpu.name, cpu_card.show()))

        if(player_card == cpu_card):
            print('\nWAR\n')
            tied = True
            war_cards = []
            while(tied):
                if(not player.has_cards() or not cpu.has_cards()):
                    tied == False
                    break

                player_card1 = player.pop_card()
                player_card2 = player.pop_card()
                cpu_card1 = cpu.pop_card()
                cpu_card2 = cpu.pop_card()

                war_cards.extend([player_card1, player_card2, cpu_card1, cpu_card2])

                if(player_card2 > cpu_card2):
                    player_stash.extend(war_cards)
                    print('\n{} Wins War'.format(player.name))
                    tied = False
                elif(player_card2 < cpu_card2):
                    cpu_stash.extend([war_cards])
                    print('\n{} Wins Round'.format(cpu.name))
                    tied = False

        elif(player_card > cpu_card):
            player_stash.extend((player_card, cpu_card))
            print('\n{} Wins Round'.format(player.name))
        else:
            cpu_stash.extend((player_card, cpu_card))
            print('\n{} Wins Round'.format(cpu.name))

        print('---------------------------------')

    

if __name__ == '__main__':
    main()