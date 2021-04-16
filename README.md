# CribbagePlayer

## Introduction
Cribbage is a two-player card game with a complicated scoring system, and asymmetrical gameplay. 
A turn has three parts, the crib, the play, and the count. The winner is the first player to score more than 120 points.

Cribbage requires players to decide what 4 cards to keep from the 6 they are dealt, while considering what card might be turned up, 
and its effects on the cards they keep. Then the players must decide how best to play their cards to capitalize on points, 
while trying to minimize how many points their opponent earns. 

## Objective
The objective of the project is to create an artificial intelligence that is able to play the game Cribbage. 
It must be able to select what cards to keep, and which to put in the kitty. 
It must be able to determine how to play its cards in order to score points, while trying to prevent the opponent from doing so.

## Future Work

The current AI does not consider how many points might be earned from playing cards when selecting a hand to keep, 
only what hands will give the most points afterwards. 
This can be very important for play near the end of the game. 
The dealer always counts hand points second, so if both players are close to winning, the dealer can prioritize trying to peg points, 
so that they can win before the opponent can count the points in their hand.

Another point of improvement is the play itself. 
Right now the AI only looks to the immediate rewards to determine what cards to play. 
Improvements can be made so that it also actively tries to avoid setting up points for the opponent. 
And an improvement to that would be plays that try to lead an opponent into setting you up, 
like setting up a double when you know you can play a triple, or a shorter run, that you could make longer. 

## Usage

The project is built using python 3, and has a dependency on the package termcolor. 
In order to run the code, install the dependency for python 3. 
The common way to install dependancies is pip, and the command would look like this:  `pip install termcolor`

The test cases can be run from test.py, `python test.py`. If all the tests pass, a message will return saying such, but if some of the cases fail, 
then an assertion error will be returned signifying which part of the code failed the test. 

The AI can be made to play a game against itself by calling cribbage.py, `python cribbage.py`. 
A log of the game will be output into the terminal, showing the round, cards dealt, how cards are discarded, 
how the hands are played, and all the scoring for the round. When one of the players reaches 121 points or more, 
the game will end, and a message saying who one will be displayed. 
