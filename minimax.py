#!/usr/bin/env python3 
# Minimax

# Module for implementation of the minimax algorithm.
import math
from engine import TicTacEngine
import logging

# returns the minimax value of a given node
def minimax(node, depth, maxPlayer):
    logging.info("Call to minimax function")
    # if node is a terminal node or depth <= 0:        
    if node.isTerminal() or depth <= 0:
        logging.info("Terminal node!")
        # return the heuristic value of node  
        logging.info("Heuristic: "+str(node.heuristic()))
        return node.heuristic()

    # Maximizing player
    if maxPlayer:
        a = -math.inf
        for child in node.get_children():          
            logging.info("Expanding node:")
            logging.info(child.board)
            logging.info("ID:"+str(child.ID))
            a = max(a, minimax( child, depth-1, False))
        return a

    # Minimizing player
    else:
        a = +math.inf
        for child in node.get_children():          
            logging.info("Expanding node:")
            logging.info(child.board)
            logging.info("ID:"+str(child.ID))
            a = min(a, minimax( child, depth-1, True) )
        return a

class node(object):
    parent = None #None = root node
    board = None # a game board
    ID = 0

    def __init__(self, parent, board):
        logging.info("Initializing new node.")
        self.parent = parent
        self.board = board
        node.ID += 1
        self.ID = node.ID


    # returns True if this is a Terminal node
    def isTerminal(self):
        return self.board.isTerminal()

    # returns the heuristic value of the node
    def heuristic(self):
        return self.board.heuristic()

    # returns the children of a node
    def get_children(self):
        children = []
        for move in self.board.getMoves():
            new_node = node(self, self.board.make_move(move))
            children.append(new_node)

        return children

# given a board object, return the best possible move to play, using the minimax algorithm
def select_move(board, isMaximizer):
    root = node(None, board)
    # list possible moves
    possibleMoves = board.getMoves()
    print("Choices:")
    print(possibleMoves)
    child_minimax = []
    # get the children and apply the minimax to each
    for child in root.get_children():
        cm = minimax(child, 15, (not isMaximizer))
        print(str(cm)+".")
        child_minimax.append(cm)

    # Best possible move, depending if caller is maximizer
    if isMaximizer:
        return possibleMoves[child_minimax.index(max(child_minimax))]
    else:
        return possibleMoves[child_minimax.index(min(child_minimax))]

# Test code
if __name__=="__main__":
    game = TicTacEngine([0,0,0,0,1,1,1,0,0],[1,0,1,1,0,0,0,0,0],1)
    #                 :X-0 1 2 3 4 5 6 7 8 O-0 1 2 3 4 5 6 7 8 turn
    print("Board state:")
    print(game)

    print("Make a node from the given board (game):")
    root = node(None, game)

    print("Calculating minimax function of root node:")
    print(minimax(root,9, True))

    print("Possible moves and their minimax value:")
    print(game.getMoves())
    possibleMoves = game.getMoves()
    child_minimax = []
    print("Moves:")
    for child in root.get_children():
        print(child.board)
        child_minimax.append(minimax(child, 9, False))
        print("Minimax as minimizer: " + str(child_minimax))

    print("Best possible move:")
    print(possibleMoves[child_minimax.index(max(child_minimax))])
