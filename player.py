from __future__ import print_function
import builtins as __builtin__
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pdb
from chess import *


class Player():
    def __init__(self,playerNum,sll):
        #sld= Starting loc list
        self.uplim=7
        self.lolim=0
        self.cmate=False
        self.check=False
        self.cemetary=dict()
        self.playerNumber=playerNum
        self.pieces=self.playerPieces(sll)
        self.poi=None

    def playerPieces(self,sll):
        ps=str(self.playerNumber)
        piecesdict={\
        'r1'+ps:Rook(self.playerNumber,'Rook',sll[0][0]),\
        'n1'+ps:Knight(self.playerNumber,'Knight',sll[0][1]),\
        'b1'+ps:Bishop(self.playerNumber,'Bishop',sll[0][2]),\
        'q1'+ps:Queen(self.playerNumber,'Queen',sll[0][3]),\
        'k1'+ps:King(self.playerNumber,'King',sll[0][4]),\
        'b2'+ps:Bishop(self.playerNumber,'Bishop',sll[0][5]),\
        'n2'+ps:Knight(self.playerNumber,'Knight',sll[0][6]),\
        'r2'+ps:Rook(self.playerNumber,'Rook',sll[0][7]),\
        'p1'+ps:Pawn(self.playerNumber,'Pawn',sll[1][0]),\
        'p2'+ps:Pawn(self.playerNumber,'Pawn',sll[1][1]),\
        'p3'+ps:Pawn(self.playerNumber,'Pawn',sll[1][2]),\
        'p4'+ps:Pawn(self.playerNumber,'Pawn',sll[1][3]),\
        'p5'+ps:Pawn(self.playerNumber,'Pawn',sll[1][4]),\
        'p6'+ps:Pawn(self.playerNumber,'Pawn',sll[1][5]),\
        'p7'+ps:Pawn(self.playerNumber,'Pawn',sll[1][6]),\
        'p8'+ps:Pawn(self.playerNumber,'Pawn',sll[1][7]),\
        }
        return piecesdict

    def removePiece(self,key):
        del self.pieces[key]

