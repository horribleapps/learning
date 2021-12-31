from __future__ import print_function
import builtins as __builtin__
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pdb
from chess import *


class Piece():
    def __init__(self,player,name,position):
        self.name=name
        self.player=player
        self.position=position
        self.r = position[0]
        self.c = position[1]
        self.pctext = {1:['[',']'],2:['=','=']}
    def availableMoves():
        print("No movement for base class")
    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        pcname= self.pctext[self.player][0]+\
                self.name+self.pctext[self.player][1]
        return pcname

class Pawn(Piece):
    def availableMoves(board):
        locs=list()
        if self.player==1:
            if x+1 <= hilim:
                if (board[x+1][y] is None):
                    locs.append([x+1,y])
                if y+1 <=hilim:
                    if (board[x+1][y+1].player is not self.player):
                        locs.append([x+1,y+1])
                if y-1 >= lolim:
                    if (board[x+1][y-1] is not self.player):
                        locs.append([x+1,y+1])
        elif self.player==2:
            if x-1 >= lolim:
                if (board[x-1][y] is None):
                    locs.append([x-1,y])
                if y-1 >= lolim:
                    if (board[x-1][y-1] is not self.player):
                        locs.append([x-1,y-1])
                if y+1 <= hilim:
                    if (board[x-1][y+1] is not self.player):
                        locs.append([x-1,y+1])
        return locs

class Rook(Piece):
    def availableMoves():
        print("Rook")

class King(Piece):
    def availableMoves():
        print("King")

class Queen(Piece):
    def availableMoves():
        print("Queen")

class Knight(Piece):
    def availableMoves():
        print("Knight")

class Bishop(Piece):
    def availableMoves():
        print("Bishop")