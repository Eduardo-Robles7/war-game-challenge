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

---

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
* **reset_hands()** - resets hand to be empty
* **has_cards()** - returns true if player has cards in hand, false otherwise 
* **card_count()** - returns count of cards in player hand

--- 

### Deck

#### Properties   
* **cards** - list of cards in deck
* **values** - list of all possible card values
* **suits**- list of all card suits

#### Methods
* **initialize_deck()** - initialize deck with every card
* **show_deck()** - displays are cards in the deck
* **shuffle_deck()** - shuffles the deck of cards
* **split_deck()** - splits deck of cards between two players

## How to run the game
The logic and setup of the game is implemented in `Main.py`.   
Game is ran in the terminal and does not need external user input.  
Currently the game is configured for two players.

In the terminal run 
```console 
python Main.py
```

## How to run unit tests
Unit tests have been written for the following classes
* Card
* Deck
* Player

Card 
```console
python test_card.py
```

Deck
```console
python test_deck.py
```

Player
```console
python test_player.py
```

## Assumptions 
* A single standard deck of 52 cards is being used.
* Two players only playing the game.
* In case of war, only two additional card are drawn, other variations draw three.
* The game ends if at any point a player runs out of cards.

## Corner cases 
* To the best of my knowledge and testing, the case of multiple wars repeating has been handled. 

## Future improvements that could be added to the game given more time
* A graphical user interface that displays users, cards, and current score.
* Allow for variations of the game to be played or customized by user.
    * Draw three additional cards instead of standard two.
    * Limit the number of wars that can occur.
    * The number of decks being used.
* Support for more than two players.
* Additional unit testing for all the functions.