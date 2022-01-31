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
        self.stalemate=False
        self.check=False
        self.userPiece=None
        self.userx=0
        self.usery=0
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

    def updateMove(self,newloc,pc):
        #if len(newloc)==1:
            #pdb.set_trace()
        if len(newloc)>0:
            x=newloc[0]
            y=newloc[1]
            cbool=False
            if not cbool:
                self.board[pc.x][pc.y]=None
                self.board[x][y]=pc
                pc.x=x;pc.y=y
        self.printBoard()

    '''def checkKing(self):
        for x in range(8):
            for y in range(8):
                pc=self.board[x][y]
                player=pc.player
                moves=pc.availableMoves(self.board)
                for m in moves:
                    moveList=self.findKing(moves,player)
                    if len(moveList)==0:
                        self.check=False
                        return None
                    else:
                if  (\
                    ()
                    )'''


    
    def findKing(self,moves,plr):
        moveList=list()
        for m in moves:
            x=m[0];y=m[1]
            if (('King' in str(self.board[x][y])) and\
                (self.board[x][y].player!=plr)):
                moveList.append([x,y])
        return moveList

    def checkKing(self,plr,moves):
        moveList=self.findKing(moves,plr)
        #pdb.set_trace()
        if len(moveList)==0:
            self.check=False
            return None
        x=moveList[0][0];y=moveList[0][1]
        #pdb.set_trace()
        kingmoves=self.board[x][y].availableMoves(self.board)
        if len(kingmoves)==0:
            self.cmate=True
        else:
            self.check=True

    def moveKing(self,plr):
        otherMoves=list()
        endTurn=False
        kingpc=None
        for i in range(8):
            for j in range(8):
                brd=self.board
                pc=self.board[i][j]
                if pc is None:
                    continue
                elif ('King' in (str(pc)) and
                    pc.player!=plr):
                    kingmoves=pc.availableMoves(self.board)
                    kingpc=pc
                elif (\
                    pc.player==plr
                    ):
                    moves=pc.availableMoves(brd)
                    if len(moves)>0:
                        otherMoves.extend(moves)
        resultingKingMoves=list()
        for km in kingmoves:
            tmp=list()
            for om in otherMoves:
                if om==km:
                    tmp.append(True)
                else:
                    tmp.append(False)
            if sum(tmp)==0:
                resultingKingMoves.extend([km])
        if len(resultingKingMoves)==0:
            self.cmate
        return resultingKingMoves,kingpc
        '''while(not endTurn):
            print("You are in check")
            tmpplr = 2 if plr==1 else 1
            print("You are player "+str(tmpplr))
            print("Available moves: ")
            print(resultingKingMoves)

        pdb.set_trace()'''


