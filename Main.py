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
        print('\n{}: {}'.format(player.name, player_card.show()))
        print('{}: {}'.format(cpu.name, cpu_card.show()))

        if(player_card == cpu_card):
            print('\n*********************************************************WAR')
            #player.add_card(player_card)
            #cpu.add_card(cpu_card)
        elif(player_card > cpu_card):
            print('\nPlayer Wins Round')
            player_stash.extend((player_card, cpu_card))
        else:
            print('\nCPU Wins Round')

        rounds = rounds + 1
     
        print('---------------------')

    

if __name__ == '__main__':
    main()