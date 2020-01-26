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
            war_cards = [player_card, cpu_card]
            while(tied):
                if(player.card_count() < 2 or cpu.card_count() < 2):
                    tied == False
                    break

                player_card1 = player.pop_card()
                player_card2 = player.pop_card()
                cpu_card1 = cpu.pop_card()
                cpu_card2 = cpu.pop_card()

                war_cards.extend([player_card1, player_card2, cpu_card1, cpu_card2])

                if(player_card2 == cpu_card2):
                    print('\nWar Again')
                elif(player_card2 > cpu_card2):
                    player_stash.extend(war_cards)
                    print('\n{} Wins War'.format(player.name))
                    tied = False
                else:
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

    if(len(player_stash) > len(cpu_stash)):
        print("\n\nWinner Player")
        print(len(player_stash))
    else:
        print('\n\nWinner CPU')
        print(len(cpu_stash))



    

if __name__ == '__main__':
    main()