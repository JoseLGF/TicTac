#!/usr/bin/env python3 

"""
Tic Tac Engine

A class to represent Tic Tac Toe Game

"""

class TicTacEngine(object):
    # the moves of the two players are represented by a list
    X = [0,0,0,0,0,0,0,0,0]
    O = [0,0,0,0,0,0,0,0,0]
    # 0 = O
    # 1 = X
    turn = 0

    # Contructor
    def __init__(self, x, o, turn):
        self.X = x
        self.O = o
        self.turn = turn
        # if not self.isValid():
        #     print('Warning, game is invalid!')

    # returns true if this is a valid tictactoe game
    def isValid(self):
        for i in range(9):
            # check that turn is valid
            if not self.turn in [0,1]:
                return False
            # check that elements of X and O are valid
            if not self.X[i] in [0,1]:
                return False
            if not self.O[i] in [0,1]:
                return False
            # check that X and O lists do not collide
            if self.X[i] == 1 and self.O[i] == 1:
                return False
        return True

    # aesthetic representation of the object
    def __repr__(self):
        ps = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        for i in range(9):
            if(self.X[i] == 1):
                ps[i] = 'X'
            if(self.O[i] == 1):
                ps[i] = 'O'

        y1 = ' 0 | 3 | 6 \n'
        y2 = '---|---|---\n'
        y3 = ' 1 | 4 | 7 \n'
        y4 = '---|---|---\n'
        y5 = ' 2 | 5 | 8 \n'
        y6 = 'Next: '

        y1 = ' '+ps[0]+' | '+ps[3]+' | '+ps[6]+'\n'
        y3 = ' '+ps[1]+' | '+ps[4]+' | '+ps[7]+'\n'
        y5 = ' '+ps[2]+' | '+ps[5]+' | '+ps[8]+'\n'
        if(self.turn == 1):
            y6 += 'X\n'
        else:
            y6 += 'O\n'

        return y1 + y2 + y3 + y4 + y5 + y6

    # returns a list with the valid moves to play for the current player
    def getMoves(self):
        moves = []

        # if there is a winner, return empty list
        # if not self.winner in [0,1]:
        #     return []

        for i in range(9):
            if (self.X[i] == 0 and self.O[i] == 0):
                moves.append(i)
        return moves

    # returns 0 if O win the game, 1 if X wins, or -1 if none
    # Assumes that the game is valid
    def winner(self):
        if( (self.X[0] == 1 and self.X[3] == 1 and self.X[6] == 1) \
        or  (self.X[1] == 1 and self.X[4] == 1 and self.X[7] == 1) \
        or  (self.X[2] == 1 and self.X[5] == 1 and self.X[8] == 1) \
        or  (self.X[0] == 1 and self.X[1] == 1 and self.X[2] == 1) \
        or  (self.X[3] == 1 and self.X[4] == 1 and self.X[5] == 1) \
        or  (self.X[6] == 1 and self.X[7] == 1 and self.X[8] == 1) \
        or  (self.X[2] == 1 and self.X[4] == 1 and self.X[6] == 1) \
        or  (self.X[0] == 1 and self.X[4] == 1 and self.X[8] == 1) ): 
            return 1
        if( (self.O[0] == 1 and self.O[3] == 1 and self.O[6] == 1) \
        or  (self.O[1] == 1 and self.O[4] == 1 and self.O[7] == 1) \
        or  (self.O[2] == 1 and self.O[5] == 1 and self.O[8] == 1) \
        or  (self.O[0] == 1 and self.O[1] == 1 and self.O[2] == 1) \
        or  (self.O[3] == 1 and self.O[4] == 1 and self.O[5] == 1) \
        or  (self.O[6] == 1 and self.O[7] == 1 and self.O[8] == 1) \
        or  (self.O[2] == 1 and self.O[4] == 1 and self.O[6] == 1) \
        or  (self.O[0] == 1 and self.O[4] == 1 and self.O[8] == 1) ): 
            return 0
        # if neither X nor O have won
        return -1

    # returns the heuristic of this game board
    # +1: X wins
    # +0: draw or game not yet finished
    # -1: O wins
    def heuristic(self):
        if (self.winner() == 1):
            return 10
        elif (self.winner() == 0):
            return -10
        else:
            return 0

    # returns Trve if this game is in a terminal state (i.e. no more moves can be made or one player has won).
    # assumes that the board is valid
    def isTerminal(self):
        if(sum(self.X)+sum(self.O) == 9):
            return True # There are moves remaining
        if(not self.winner()==-1):
            return True # One of the two players has won
        else:
            return False

    # Returns a TicTacEngine object after a move has been made
    # If the move is not valid, a copy of self is returned
    def make_move(self, move):
        if not move in self.getMoves():
            return TicTacEngine(self.X,self.O,self.turn)

        # build the new board with the move
        new_X = self.X.copy()
        new_O = self.O.copy()
        new_turn = self.turn

        # write the move
        if(self.turn==0):
            new_O[move] = 1
        else:
            new_X[move] = 1

        # switch turn
        if(self.turn ==0):
            new_turn = 1
        else:
            new_turn = 0

        # build and return the new objet
        return TicTacEngine(new_X,new_O,new_turn)

# Test code
if __name__ == "__main__":
    # instantiate a valid game
    tt1 = TicTacEngine([1,0,1,0,1,0,1,0,1],[0,1,0,1,0,1,0,1,0],0)
    print(tt1)
    print(tt1.isValid())
    # instantiate an invalid game
    tt2 = TicTacEngine([1,1,1,1,1,0,1,0,1],[0,1,0,1,0,1,0,1,0],0)
    print(tt2)
    print(tt2.isValid())
    # instantiate empty game
    tt3 = TicTacEngine([0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],0)
    print(tt3)
    print(tt3.isValid())
    print(tt3.getMoves())
    # instantiate valid game
    print("4:")
    tt4 = TicTacEngine([1,1,0,0,0,1,0,0,0],[0,0,1,0,0,0,1,0,0],0)
    print(tt4)
    print(tt4.isValid())
    print(tt4.getMoves())
    print(tt4.winner())
    # instantiate valid game, where X has won
    print("5:")
    print("Object:")
    tt5 = TicTacEngine([1,1,1,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0],0)
    print(tt5)
    print("isValid Method:")
    print(tt5.isValid())
    print("getMoves()")
    print(tt5.getMoves())
    print("winner()")
    print(tt5.winner())
    print("isTerminal()")
    print(tt5.isTerminal())

    print("6:")
    print("Object:")
    dum = TicTacEngine([0,1,1,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0],0)
    print(dum)
    print("isValid Method:")
    print(dum.isValid())
    print("getMoves()")
    print(dum.getMoves())
    print("winner()")
    print(dum.winner())
    print("isTerminal()")
    print(dum.isTerminal())
    print("moves in square 0")
    print(dum.make_move(0))

    print("result's properties:")

    print("6's kid:")
    print("Object:")
    kid = dum.make_move(0)
    print(kid)
    print("isValid Method:")
    print(kid.isValid())
    print("getMoves()")
    print(kid.getMoves())
    print("winner()")
    print(kid.winner())
    print("isTerminal()")
    print(kid.isTerminal())
    print("moves in square 8")
    print(kid.make_move(8))

    print("kid's kid:")
    print("Object:")
    gsn = kid.make_move(8)
    print(gsn)
    print("isValid Method:")
    print(gsn.isValid())
    print("getMoves()")
    print(gsn.getMoves())
    print("winner()")
    print(gsn.winner())
    print("isTerminal()")
    print(gsn.isTerminal())
    # print("moves in square 8")
    # print(gsn.make_move(8))
