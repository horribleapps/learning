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
        self.x = position[0]
        self.y = position[1]
        self.availableLocs=list()
        self.pctext = {1:['[',']'],2:['=','=']}
        self.uplim=7
        self.lolim=0
        self.locs=list()
    def availableMoves(self):
        print("No movement for base class")

    def checkBounds(self,intervals):
        inBoundIntervals=list()
        for lx,ly in intervals:
            if (lx>=self.lolim) and (ly>=self.lolim) and (lx<=self.uplim) and (ly<=self.uplim):
                inBoundIntervals.append([lx,ly])
        return inBoundIntervals

    def checkpiece(self,board,intervals):
        #print(str(px)+' '+str(py))
        trimIntervals=list()
        for i in intervals:
            if len(i)>0:
                breakbool=False
                for jx,jy in i:  
                    if board[jx][jy] is None and not breakbool:
                        trimIntervals.append([jx,jy])
                    elif board[jx][jy].player!=self.player and not breakbool:
                        trimIntervals.append([jx,jy])
                    else:
                        breakbool=True
                        break
        return trimIntervals

    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        pcname= self.pctext[self.player][0]+\
                self.name+self.pctext[self.player][1]
        return pcname

class Pawn(Piece):
    self.moveNum=1
    def availableMoves(self,board):
        locs=list()
        x=self.x
        y=self.y
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
            if x+2 <= hilim:
                if board[x+2][y] is None and self.moveNum==1:
                    locs.append([x+2,y])
                    self.moveNum+=1
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
            if x-2 <= lolim:
                if board[x-2][y] is None and self.moveNum==1:
                    locs.append([x-2,y])
                    self.moveNum+=1
        self.availableLocs=locs
        return locs

class Rook(Piece):
    
    def availableMoves(self,board):
        #print("rook")
        x=self.x
        y=self.y
        locs=list()
        inBoundIntervals=list()
        #looking at values greater than x
        inBoundIntervals.append(self.checkBounds([[px,y] for px in range(x+1,self.uplim+1)]))
        inBoundIntervals.append(self.checkBounds([[x,py] for py in range(y+1,self.uplim+1) ]))
        inBoundIntervals.append(self.checkBounds([[px,y] for py in reversed(range(self.lolim,x)) ]))
        inBoundIntervals.append(self.checkBounds([[x,py] for py in reversed(range(self.lolim,y)) ]))
        trimIntervals=self.checkpiece(board,inBoundIntervals)
        self.availableLocs=trimIntervals
        return trimIntervals

class King(Piece):
    def availableMoves(self):
        print("King")
        #print("rook")
        x=self.x
        y=self.y
        locs=list()
        inBoundIntervals=list()
        inBoundIntervals.append(\
                                self.checkBounds( \
                                [[x+1,py] for py in range(y-1,y+1)]\
                                )\
                                )
        inBoundIntervals.append(\
                                self.checkBounds( \
                                [[x-1,py] for py in range(y-1,y+1)]\
                                )\
                                )
        inBoundIntervals.append(\
                                self.checkBounds( \
                                [[x,py] for py in [y-1,y+1] ]\
                                )\
                                )
        trimIntervals=self.checkpiece(board,inBoundIntervals)
        self.availableLocs=trimIntervals
        return trimIntervals

class Queen(Piece):
    def availableMoves(self,board):
        #print("rook")
        x=self.x
        y=self.y
        locs=list()
        inBoundIntervals=list()
        #looking at values greater than x
        inBoundIntervals.append(self.checkBounds([[px,y] for px in range(x+1,self.uplim+1)]))
        inBoundIntervals.append(self.checkBounds([[x,py] for py in range(y+1,self.uplim+1) ]))
        inBoundIntervals.append(self.checkBounds([[px,y] for py in reversed(range(self.lolim,x)) ]))
        inBoundIntervals.append(self.checkBounds([[x,py] for py in reversed(range(self.lolim,y)) ]))
        #x+px, x+py
        inBoundIntervals.append(\
                                self.checkBounds(\
                                [ [x+px,y+py] for px,py in zip(range(1,8),range(1,8)) ]\
                                ))
        #x-px, x-py
        inBoundIntervals.append(\
                                self.checkBounds(\
                                [ [x-px,y-py] for px,py in zip(\
                                range(1,8),range(1,8) \
                                ) ]\
                                ))
        #x-px, x+py
        inBoundIntervals.append(\
                                self.checkBounds(\
                                [ [x-px,y+py] for px,py in zip(\
                                range(1,8),range(1,8) \
                                ) ]\
                                ))
        #x+px, x-py
        inBoundIntervals.append(\
                                self.checkBounds(\
                                [ [x+px,y-py] for px,py in zip(\
                                range(1,8),range(1,8) \
                                ) ]\
                                ))
        trimIntervals=self.checkpiece(board,inBoundIntervals)
        self.availableLocs=trimIntervals
        return trimIntervals

class Knight(Piece):
    def availableMoves(self):
        #print("rook")
        x=self.x
        y=self.y
        locs=list()
        inBoundIntervals=list()
        #x+px, x+py
        inBoundIntervals.append(\
                                self.checkBounds(\
                                [ [x+px,y+py] for px,py in zip(range(1,8),range(1,8)) ]\
                                ))
        #x-px, x-py
        inBoundIntervals.append(\
                                self.checkBounds(\
                                [ [x-px,y-py] for px,py in zip(\
                                range(1,8),range(1,8) \
                                ) ]\
                                ))
        #x-px, x+py
        inBoundIntervals.append(\
                                self.checkBounds(\
                                [ [x-px,y+py] for px,py in zip(\
                                range(1,8),range(1,8) \
                                ) ]\
                                ))
        #x+px, x-py
        inBoundIntervals.append(\
                                self.checkBounds(\
                                [ [x+px,y-py] for px,py in zip(\
                                range(1,8),range(1,8) \
                                ) ]\
                                ))
        trimIntervals=self.checkpiece(board,inBoundIntervals)
        self.availableLocs=trimIntervals
        return trimIntervals


class Bishop(Piece):
    def availableMoves(self,board):
        #print("rook")
        x=self.x
        y=self.y
        locs=list()
        inBoundIntervals=list()
        #x+px, x+py
        inBoundIntervals.append(\
                                self.checkBounds( \
                                [[x+2,py] for py in range(y-1,y+1)]\
                                )\
                                )
        inBoundIntervals.append(\
                                self.checkBounds( \
                                [[x-2,py] for py in range(y-1,y+1)]\
                                )\
                                )
        inBoundIntervals.append(\
                                self.checkBounds( \
                                [[px,y+2] for px in range(x-1,x+1)]\
                                )\
                                )
        inBoundIntervals.append(\
                                self.checkBounds( \
                                [[px,y-2] for px in range(x-1,x+1)]\
                                )\
                                )       
        trimIntervals=self.checkpiece(board,inBoundIntervals)
        self.availableLocs=trimIntervals
        return trimIntervals
