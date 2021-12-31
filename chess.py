from __future__ import print_function
import builtins as __builtin__
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pdb
from piece import *


class Game():
    def __init__(self):
        self.board= [\
                    [None, None, None, None, None, None, None, None],\
                    [None, None, None, None, None, None, None, None],\
                    [None, None, None, None, None, None, None, None],\
                    [None, None, None, None, None, None, None, None],\
                    [None, None, None, None, None, None, None, None],\
                    [None, None, None, None, None, None, None, None],\
                    [None, None, None, None, None, None, None, None],\
                    [None, None, None, None, None, None, None, None],\
        ]
        self.uplim=7
        self.lolim=0
        self.cmate=False
        self.placePieces()
        self.printBoard()
    
    def placePieces(self):
        pl=1
        self.board[0]=  [ \
                        Rook(pl,'Rook',     (0,0)), \
                        Knight(pl,'Knight', (0,1)), \
                        Bishop(pl,'Bishop', (0,2)), \
                        Queen(pl,'Queen',   (0,3)), \
                        King(pl,'King',     (0,4)), \
                        Bishop(pl,'Bishop', (0,5)), \
                        Knight(pl,'Knight', (0,6)), \
                        Rook(pl,'Rook',     (0,7)), \
                        ]
        self.board[1]=  [ \
                        Pawn(pl,'Pawn',(1,0)), \
                        Pawn(pl,'Pawn',(1,1)), \
                        Pawn(pl,'Pawn',(1,2)), \
                        Pawn(pl,'Pawn',(1,3)), \
                        Pawn(pl,'Pawn',(1,4)), \
                        Pawn(pl,'Pawn',(1,5)), \
                        Pawn(pl,'Pawn',(1,6)), \
                        Pawn(pl,'Pawn',(1,7)), \
                        ]
        pl=2
        self.board[-1]= [ \
                        Rook(pl,'Rook',     (7,0)), \
                        Knight(pl,'Knight', (7,1)), \
                        Bishop(pl,'Bishop', (7,2)), \
                        Queen(pl,'Queen',   (7,3)), \
                        King(pl,'King',     (7,4)), \
                        Bishop(pl,'Bishop', (7,5)), \
                        Knight(pl,'Knight', (7,6)), \
                        Rook(pl,'Rook',     (7,7)), \
                        ]
        self.board[6]=  [ \
                        Pawn(pl,'Pawn',(6,0)), \
                        Pawn(pl,'Pawn',(6,1)), \
                        Pawn(pl,'Pawn',(6,2)), \
                        Pawn(pl,'Pawn',(6,3)), \
                        Pawn(pl,'Pawn',(6,4)), \
                        Pawn(pl,'Pawn',(6,5)), \
                        Pawn(pl,'Pawn',(6,6)), \
                        Pawn(pl,'Pawn',(6,7)), \
                        ]

    def printBoard(self):
        print('|'.center(1),end="")
        for i in range(0,8):
            strpc = str(i).center(8)
            print(strpc,end="")
            print(' | '.center(1),end="")
        print()
        for i in range(0,8):
            print('|'.center(1),end="")
            for j in range(0,8):
                print(str(self.board[i][j]).center(8),end="")
                print(' | ',end="")
            print(str(i).center(3),end="")
            print()

    def check(self,newloc,pc):
        x=newloc[0]
        y=newloc[1]
        if ('King' in str(self.board[x][y])) and (pc.player!=self.board[x][y].player):
            self.cmate=True
            return True
        else:
            self.cmate=False
            return False


    def updateMove(self,newloc,pc):
        print("h")
        if len(newloc)>0:
            x=newloc[0]
            y=newloc[1]
            cbool=self.check(newloc,pc)
            if ~cbool:
                self.board[pc.x][pc.y]=None
                self.board[x][y]=pc
                pc.x=x;pc.y=y
        self.printBoard()

#gm=Game()
#rk=gm.board[0][7]
#print(rk.availableMoves(gm.board))

