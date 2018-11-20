#!/usr/bin/env python3 

# tic tac toe implementation

from engine import TicTacEngine 
import minimax

print("TicTacToe Game:")

next_player = -1
computer_bhv = ''

while(not next_player in ['0', '1']):
    print("Who starts? 0-Computer, 1-Human.")
    next_player = input()

if(next_player=='0'):
    isMaximizer = False
else:
    isMaximizer = True
    

# create new empty board
game = TicTacEngine([0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],0)

while not game.isTerminal():
    if next_player == '0':
        # computer is next
        # ask computer for next move
        comp_move = minimax.select_move(game, isMaximizer)
        print("Computer plays: " + str(comp_move))
        game = game.make_move(comp_move)
        next_player = '1'
    
    else:
        # human is next
        # ask human for next move
        move = -1
        valid = False
        while not valid:
            # ask input
            while not move in range(9):
                move = int(input("Enter your move (0-8)"))
            # check input
            if move in game.getMoves():
                valid = True
            else:
                move = -1

        game = game.make_move(move)
        next_player = '0'
    print(game)


print("Game finished")
