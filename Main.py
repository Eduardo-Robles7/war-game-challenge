from Card import Card
from Deck import Deck
from Player import Player

def display_user(player,card):
    """Displays player name and current card"""
    print('{}: {}\n'.format(player.name, card.show()))

def display_war_winner(name):
    """Displays winner of war tie"""
    print('\n{} Wins War'.format(name))

def display_round_winner(name):
    """Displays winner of the round"""
    print('\n{} Wins Round'.format(name))

def main():    
    #setup players
    player = Player('Eduardo')
    cpu = Player('Intel')

    #setup deck and stashes
    deck = Deck()
    deck.initialize_deck()
    deck.shuffle_deck()
    deck.split_deck(player, cpu)
    player_stash = []
    cpu_stash = [] 

    #run until a player runs out of cards
    while player.has_cards() and cpu.has_cards():
        #draw initial cards
        player_card = player.pop_card()
        cpu_card = cpu.pop_card()
        display_user(player, player_card)
        display_user(cpu, cpu_card)

        #check for war
        if(player_card == cpu_card):
            print('!!!WAR!!!\n')
            tied = True
            war_cards = [player_card, cpu_card]
            while(tied):

                #end game if either player runs out of cards
                if(player.card_count() < 2 or cpu.card_count() < 2):
                    print('Game over out of cards')
                    tied == False
                    break

                #draw two additional cards
                player_card1 = player.pop_card()
                player_card2 = player.pop_card()
                cpu_card1 = cpu.pop_card()
                cpu_card2 = cpu.pop_card()
                display_user(player, player_card2)
                display_user(cpu, cpu_card2)
                war_cards.extend([player_card1, player_card2, cpu_card1, cpu_card2])

                #check for war again
                if(player_card2 == cpu_card2):
                    print('\nWar Again')

                #player wins
                elif(player_card2 > cpu_card2):
                    player_stash.extend(war_cards)
                    display_war_winner(player.name)
                    tied = False

                #cpu wins
                else:
                    cpu_stash.extend([war_cards])
                    display_war_winner(cpu.name)
                    tied = False

        #player wins
        elif(player_card > cpu_card):
            player_stash.extend((player_card, cpu_card))
            display_round_winner(player.name)
        
        #cpu wins
        else:
            cpu_stash.extend((player_card, cpu_card))
            display_round_winner(cpu.name)

        print('---------------------------------')

    #Check for winner
    if(len(player_stash) > len(cpu_stash)):
        print('\nWinner: {}'.format(player.name))
        print('Score: {} cards'.format(len(player_stash)))
    else:
        print('\nWinner: {}'.format(cpu.name))
        print('Score: {} cards'.format(len(cpu_stash)))


if __name__ == '__main__':
    main()