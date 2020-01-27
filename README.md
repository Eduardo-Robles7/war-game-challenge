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

### Deck

