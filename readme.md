# Tic Tac Engine Using MiniMax algorithm

Python implementation of the minimax algorithm for the tic tac toe game.

## Tic Tac Engine

First of all, a Tic Tac Engine is needed.
The file [engine.py](https://github.com/LuisGerman92/TicTac/blob/master/engine.py) contains a class for implementing the Tic Tac Toe game.

In order to represent any possible state of the game, the moves by the X player, the moves by the O player, and the turn, i.e. who plays next, are needed.

Some basic methods allow us to obtain information about the game, such as `isValid`, `getMoves`, `winner`, etc.

The method `make\_move` will, instead of modifying the current object, return a copy of the class, in which the desired move has been made.

## minimax module

This module is intended for the actual implementation of the minimax algorithm.
Not only does it contain the `minimax` function, and the `node` class it uses to work, but also an agent (function) that, when passed a board, it will return the optimal move, depending on if he is a maximizer, or a minimizer.

### Minimax function

This is the function implementation of the minimax algorithm, in which the heuristic value for the nodes are returned recursively.

## game

This is a very simple program that takes user input in order to play the game against the computer agent.
In order to see the program in action, run in the terminal:
```console
./game.py
```
