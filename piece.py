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
        self.moveNum=0
        self.seeKing=False

    def availableMoves(self):
        print("No movement for base class")

    def checkBounds(self,intervals):
        inBoundIntervals=list()
        for lx,ly in intervals:
            if (lx>=self.lolim) and (ly>=self.lolim) and (lx<=self.uplim) and (ly<=self.uplim):
                inBoundIntervals.append([lx,ly])
        return inBoundIntervals

    def checkpiece(self,board,intervals):
        trimIntervals=list()
        for i in intervals:
            if len(i)>0:
                breakbool=False
                for jx,jy in i:  
                    if board[jx][jy] is None and not breakbool:
                        trimIntervals.append([jx,jy])
                    elif board[jx][jy].player!=self.player and not breakbool:
                        trimIntervals.append([jx,jy])
                        return trimIntervals
                    else:
                        breakbool=True
                        break
        return trimIntervals

    def checkKing(self,board):
        intervals = self.availableLocs
        cntr=0
        if len(intervals)>0:
            for kx,ky in intervals:
                if (('King' in str(board[kx][ky])) and \
                    (board[kx][ky].player != self.player)):
                    self.seeKing=True
                    #pdb.set_trace()
                    break
        if cntr==len(intervals):
            self.seeKing=False

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        pcname= self.pctext[self.player][0]+\
                self.name+self.pctext[self.player][1]
        return pcname

class Pawn(Piece):

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

    def availableMoves(self,board):
        locs=list()
        x=self.x
        y=self.y
        if self.player==1:
            if x+1 <= self.uplim:
                if (board[x+1][y] is None):
                    locs.append([x+1,y])
                if y+1 <=self.uplim:
                    if board[x+1][y+1] is not None:
                        if (board[x+1][y+1].player is not self.player):
                            locs.append([x+1,y+1])
                if y-1 >= self.lolim:
                    if board[x+1][y-1] is not None:
                        if (board[x+1][y-1].player is not self.player):
                            locs.append([x+1,y-1])
            #if x+2 <= self.uplim:
            #    if board[x+2][y] is None and self.moveNum==0:
            #        locs.append([x+2,y])
            #        self.moveNum+=1
        elif self.player==2:
            if x-1 >= self.lolim:
                if (board[x-1][y] is None):
                    locs.append([x-1,y])
                if y-1 >= self.lolim:
                    if board[x-1][y-1] is not None:
                        if (board[x-1][y-1].player is not self.player):
                            locs.append([x-1,y-1])
                if y+1 <= self.uplim:
                    if board[x-1][y+1] is not None:
                        if (board[x-1][y+1].player is not self.player):
                            locs.append([x-1,y+1])
            #if x-2 <= self.lolim:
            #    if board[x-2][y] is None and self.moveNum==1:
            #        locs.append([x-2,y])
            #        self.moveNum+=1
        self.availableLocs=locs
        self.checkKing(board)
        return locs

class Rook(Piece):
    

    def availableMoves(self,board):
        #print("rook")
        x=self.x
        y=self.y
        locs=list()
        inBoundIntervals1=list()
        inBoundIntervals2=list()
        inBoundIntervals3=list()
        inBoundIntervals4=list()
        #looking at values greater than x
        inBoundIntervals1.append(self.checkBounds([[px,y] for px in range(x+1,self.uplim+1)]))
        trimIntervals1 = self.checkpiece(board,inBoundIntervals1)
        inBoundIntervals2.append(self.checkBounds([[x,py] for py in range(y+1,self.uplim+1) ]))
        trimIntervals2 = self.checkpiece(board,inBoundIntervals2)
        inBoundIntervals3.append(self.checkBounds([[px,y] for px in reversed(range(self.lolim,x)) ]))
        trimIntervals3 = self.checkpiece(board,inBoundIntervals3)
        inBoundIntervals4.append(self.checkBounds([[x,py] for py in reversed(range(self.lolim,y)) ]))
        trimIntervals4 = self.checkpiece(board,inBoundIntervals4)
        trimIntervals=trimIntervals1+trimIntervals2+trimIntervals3+trimIntervals4
        #trimIntervals=self.checkpiece(board,inBoundIntervals)
        self.availableLocs=trimIntervals
        self.checkKing(board)
        return trimIntervals

class King(Piece):

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
        return trimIntervals

    def availableMoves(self,board):
        print("King")
        #print("rook")
        x=self.x
        y=self.y
        locs=list()
        inBoundIntervals=list()
        inBoundIntervals.append(\
                                self.checkBounds( \
                                [[x+1,py] for py in range(y-1,y+2)]\
                                )\
                                )
        inBoundIntervals.append(\
                                self.checkBounds( \
                                [[x-1,py] for py in range(y-1,y+2)]\
                                )\
                                )
        inBoundIntervals.append(\
                                self.checkBounds( \
                                [[x,py] for py in range(y-1,y+2) ]\
                                )\
                                )
        trimIntervals=self.checkpiece(board,inBoundIntervals)
        self.availableLocs=trimIntervals
        self.checkKing(board)
        return trimIntervals

class Queen(Piece):
    def availableMoves(self,board):
        #print("rook")
        x=self.x
        y=self.y
        locs=list()
        inBoundIntervals1=list()
        inBoundIntervals2=list()
        inBoundIntervals3=list()
        inBoundIntervals4=list()
        inBoundIntervals5=list()
        inBoundIntervals6=list()
        inBoundIntervals7=list()
        inBoundIntervals8=list()
        #looking at values greater than x
        inBoundIntervals1.append(self.checkBounds([[px,y] for px in range(x+1,self.uplim+1)]))
        trimIntervals1 = self.checkpiece(board,inBoundIntervals1)
        inBoundIntervals2.append(self.checkBounds([[x,py] for py in range(y+1,self.uplim+1) ]))
        trimIntervals2 = self.checkpiece(board,inBoundIntervals2)
        inBoundIntervals3.append(self.checkBounds([[px,y] for px in reversed(range(self.lolim,x)) ]))
        trimIntervals3 = self.checkpiece(board,inBoundIntervals3)
        inBoundIntervals4.append(self.checkBounds([[x,py] for py in reversed(range(self.lolim,y)) ]))
        trimIntervals4 = self.checkpiece(board,inBoundIntervals4)
        #x+px, x+py
        inBoundIntervals5.append(\
                                self.checkBounds(\
                                [ [x+px,y+py] for px,py in zip(range(1,8),range(1,8)) ]\
                                ))
        trimIntervals5 = self.checkpiece(board,inBoundIntervals5)
        #x-px, x-py
        inBoundIntervals6.append(\
                                self.checkBounds(\
                                [ [x-px,y-py] for px,py in zip(\
                                range(1,8),range(1,8) \
                                ) ]\
                                ))
        trimIntervals6 = self.checkpiece(board,inBoundIntervals6)
        #x-px, x+py
        inBoundIntervals7.append(\
                                self.checkBounds(\
                                [ [x-px,y+py] for px,py in zip(\
                                range(1,8),range(1,8) \
                                ) ]\
                                ))
        trimIntervals7 = self.checkpiece(board,inBoundIntervals7)
        #x+px, x-py
        inBoundIntervals8.append(\
                                self.checkBounds(\
                                [ [x+px,y-py] for px,py in zip(\
                                range(1,8),range(1,8) \
                                ) ]\
                                ))
        trimIntervals8 = self.checkpiece(board,inBoundIntervals8)
        trimIntervals=trimIntervals1+trimIntervals2+trimIntervals3+\
                        trimIntervals4+trimIntervals5+trimIntervals6+\
                        trimIntervals7+trimIntervals8
        #trimIntervals=self.checkpiece(board,inBoundIntervals)
        self.availableLocs=trimIntervals
        self.checkKing(board)
        return trimIntervals

class Knight(Piece):

    def __init__(self,player,name,position):
        super().__init__(player,name,position)
        self.check=False
        self.cmate=False
    
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

    def availableMoves(self,board):
        #print("rook")
        x=self.x
        y=self.y
        locs=list()
        inBoundIntervals=list()
        #x+2, x+py
        inBoundIntervals.append(\
                                self.checkBounds(\
                                [ [x+2,y+py] for py in [-1,1] ]\
                                ))
        #x-2, x+py
        inBoundIntervals.append(\
                                self.checkBounds(\
                                [ [x-2,y+py] for py in [-1,1]]\
                                ))
        #x-px, x+py
        inBoundIntervals.append(\
                                self.checkBounds(\
                                [ [x+px,y+2] for px in [-1,1]]\
                                ))
        #x+px, x-py
        inBoundIntervals.append(\
                                self.checkBounds(\
                                [ [x+px,y-2] for px in [-1,1] ]\
                                ))
        trimIntervals=self.checkpiece(board,inBoundIntervals)
        self.availableLocs=trimIntervals
        self.checkKing(board)
        return trimIntervals

    def isCheck(self,board):
        #moveList=self.findKing(moves,plr)
        tmplist=list()
        for i in range(8):
            for j in range(8):
                pc=board[i][j]
                if (pc.player!=player):
                    tmplist.append(pc.availableMoves(board))
        
        
        '''tmplist=list()
        for k in otherPlayer.pieces:
            tmplist.extend(otherplayer.pieces[k].availableMoves(board))
        kingmoves=self.pieces['k1'+str(self.playerNumber)]\
                            .availableMoves(board)
        if len(kingmoves)==0:
            self.cmate=True
        resultingMoves=list()
        boolList=list()
        for km in kingmoves:
            for m in tmplist:
                boolList.append(m==km)
            if sum(boolList)!=0:
                resultingMoves.extend(km)
        if len(resultingMoves)==0:
            self.cmate=True
        else:
            self.check=True'''

class Bishop(Piece):

    def availableMoves(self,board):
        #print("rook")
        x=self.x
        y=self.y
        locs=list()
        inBoundIntervals1=list()
        inBoundIntervals2=list()
        inBoundIntervals3=list()
        inBoundIntervals4=list()
        #x+px, x+py
        inBoundIntervals1.append(\
                                self.checkBounds(\
                                [ [x+px,y+py] for px,py in zip(range(1,8),range(1,8)) ]\
                                ))
        trimIntervals1 = self.checkpiece(board,inBoundIntervals1)
        #x-px, x-py
        inBoundIntervals2.append(\
                                self.checkBounds(\
                                [ [x-px,y-py] for px,py in zip(\
                                range(1,8),range(1,8) \
                                ) ]\
                                ))
        trimIntervals2 = self.checkpiece(board,inBoundIntervals2)
        #x-px, x+py
        inBoundIntervals3.append(\
                                self.checkBounds(\
                                [ [x-px,y+py] for px,py in zip(\
                                range(1,8),range(1,8) \
                                ) ]\
                                ))
        trimIntervals3 = self.checkpiece(board,inBoundIntervals3)
        #x+px, x-py
        inBoundIntervals4.append(\
                                self.checkBounds(\
                                [ [x+px,y-py] for px,py in zip(\
                                range(1,8),range(1,8) \
                                ) ]\
                                ))
        trimIntervals4 = self.checkpiece(board,inBoundIntervals4)
        trimIntervals=trimIntervals1+trimIntervals2+trimIntervals3+trimIntervals4
        #trimIntervals=self.checkpiece(board,inBoundIntervals)
        self.availableLocs=trimIntervals
        self.checkKing(board)
        return trimIntervals
