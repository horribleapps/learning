from __future__ import print_function
import builtins as __builtin__
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pdb
import random
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
        f=open('moves.txt','w')  
        f.close()
        self.uplim=7
        self.lolim=0
        self.cmate=False
        self.check=False
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
        f = open('moves.txt','a')
        startingdiv='|'.center(1)
        print(startingdiv,end="");f.write(startingdiv)
        for i in range(0,8):
            strpc = str(i).center(8)
            print(strpc,end="");f.write(strpc)
            div1=' | '.center(1)
            print(div1,end="");f.write(div1)
        nline="\n"
        print(nline,end="");f.write(nline)
        for i in range(0,8):
            div2='|'.center(1)
            print(div2,end="");f.write(div2)
            for j in range(0,8):
                stroi=str(self.board[i][j]).center(8)
                print(stroi,end="");f.write(stroi)
                div3=' | '
                print(div3,end="");f.write(div3)
            yidx=str(i).center(3)
            print(yidx,end="");f.write(yidx)
            print(nline,end="");f.write(nline)
        f.write("==============================\n")
        f.write("==============================\n")
        f.write("==============================\n")
        f.close()

    def verifyCheck(self,newloc,pc):
        x=newloc[0]
        y=newloc[1]
        
        for i in range(0,8):
            for j in range(0,8):
                tmp=self.board[i][j]
                if tmp is not None:
                    xyvals=tmp.availableMoves(self.board)
                else:
                    continue
                for kx,ky in xyvals:
                    if ('King' in str(self.board[kx][ky])):
                        pdb.set_trace()
                    if  (\
                        ('King' in str(self.board[kx][ky])) \
                        and \
                        (self.board[kx][ky].player != pc.player) \
                        ):
                        
                        kingtmp=self.board[kx][ky]
                        kingAvailableMoves=kingtmp.availableMoves(self.board)
                        pdb.set_trace()
                        if len(kingAvailableMoves)==0:
                            self.cmate=True
                            return True
                        newKingMove=random.choice(kingAvailableMoves)
                        self.moveKing(newKingMove,kingtmp)
                        self.check=True
                        return True
                    else:
                        self.check=False
                        return False

    def updateMove(self,newloc,pc):
        if len(newloc)>0:
            x=newloc[0]
            y=newloc[1]
            #cbool=self.verifyCheck(newloc,pc)
            cbool=False
            if not cbool:
                self.board[pc.x][pc.y]=None
                self.board[x][y]=pc
                pc.x=x;pc.y=y
        self.printBoard()

    def kingInCheck(self,pc,board):
        intervals = pc.availableLocs
        cntr=0
        if len(intervals)>0:
            for kx,ky in intervals:
                if board[kx][ky] is not None:
                    continue
                    if (\
                    ('King' in str(board[kx][ky])) \
                    and \
                    (board[kx][ky].player != self.player)\
                    ):
                        pck=board[kx][ky]
                        kam=pck.availableMoves(board)
                        pdb.set_trace()
                        if len(kam) == 0:
                            self.cmate=True
                            break
                        elif len(kam) ==1:
                            updateMove(kam,pck)
                            break
                        elif len(kam) > 0:
                            pcloc=random.choice(kam)
                            updateMove(kam,pck)
                            break
        '''
        x=newloc[0]
        y=newloc[1]
        self.board[pc.x][pc.y]=None
        self.board[x][y]=pc
        pc.x=x;pc.y=y
        '''

#gm=Game()
#rk=gm.board[0][7]
#print(rk.availableMoves(gm.board))

