# War Game Coding Challenge
This is an implementation of the card game War.   
Python was the selected language of choice with no additional external libraries.


## Rules
1. Objective of game is to win all of the cards.
2. Deck is divided evenly among two players.
3. Each player reveals the top card of their deck.
4. Player with the higher card takes both of the cards played and moves them into their pile.
5. If two cards are the same value, then a war takes place.
    * Both players place draw two additional cards, 1 hidden and 1 revealed.
    * Player with higher revealed card wins war and moves all cards into their pile. 
    * If a war takes place again, The battle repeats with players drawing two additional cards.
    * This repeats until one player has a higher card than their opponents. 

More information on rules [(Wiki War Card Game)](https://en.wikipedia.org/wiki/War_(card_game))

## Design & Implementation
Object-oriented design was used to split the game into various classes for objects.   
Each component of the game is implemented with its own class. This allows for more simplicity and future extensibility.   
Data is encapsulated  and handled by class methods. 

## Classes

### Card
Represents a single card in the deck. 

#### Properties
* **value** - numerical value of card
* **suit** - the suit of the card

#### Methods
* **show()** - returns string containing value and suit of card
* **get_value()** - returns the value of the card

### Player
Represents a single player in the game. Each player has a name and a hand of cards. 

#### Properties
* **name** - name of player
* **hand** - list of cards player has in hand

#### Methods
* **show_hand()** - displays all cards in player hand
* **add_card(card)** - adds a card to the player hand
* **add_cards(cards)** - adds a list of cards to the player hand
* **pop_card()** - returns the top card from hand 
* **reset_hands()** - resets haand to be empty
* **has_cards()** - returns true if player has cards in hand, false otherwise 
* **card_count()** - returns count of cards in player hand

### Deck

#### Properties   
* **cards** - list of cards in deck
* **values** - list of all possible card values
* **suits**- list of all card suits

#### Methods
* **initialize_deck()** - initializes deck with every card
* **show_deck()** - displays are cards in the deck
* **shuffle_deck()** - shuffles the deck of cards
* **split_deck()** - splits deck of cards between two players

