from __future__ import print_function
import builtins as __builtin__
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pdb
import random
from piece import *
from player import *


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
        self.userPiece=None
        self.userx=0
        self.usery=0
        self.player1=None
        self.player2=None
        self.initplacePieces()
        self.printBoard()
        self.cmate=False
        self.etp1=False #etp1=endTurnPlayer1
        self.etp2=False #etp2=endTurnPlayer2

    def initplacePieces(self):
        p1list=list();p2list=list()
        p1list.append([(0,y) for y in range(8)])
        p1list.append([(1,y) for y in range(8)])
        self.player1=Player(1,p1list)
        p2list.append([(7,y) for y in range(8)])
        p2list.append([(6,y) for y in range(8)])
        self.player2=Player(2,p2list)

    def fillBoard(self):
        for k in self.player1.pieces:
            self.board\
            [self.player1.pieces[k].x]\
            [self.player1.pieces[k].y]=\
            self.player1.pieces[k]
        for k in self.player2.pieces:
            self.board\
            [self.player2.pieces[k].x]\
            [self.player2.pieces[k].y]=\
            self.player2.pieces[k]

    def printBoard(self):
        self.fillBoard()
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

    def checkKing(self):
        p1moves=list();p2moves=list()
        #pdb.set_trace()
        print("check: player1, player2")
        self.findKing(self.player1,self.player2)
        print("check: player2, player1")
        self.findKing(self.player2,self.player1)
    
    def findKing(self,plroi,opponent):
        pmoves=list()
        pn=plroi.playerNumber
        spn=str(plroi.playerNumber)
        for k in opponent.pieces:
            pmoves.extend(\
            opponent.pieces[k]\
            .availableMoves(self.board))
        kmoves=plroi.pieces['k1'+spn].availableMoves(self.board)
        kxy=[[plroi.pieces['k1'+spn].x,plroi.pieces['k1'+spn].y]]
        kplacesum=sum([x==kxy[0] for x in pmoves])
        availKingMoves=self.comparearr(pmoves,kmoves)
        if len(availKingMoves)==0 and len(kmoves)>0\
            and\
            kplacesum>0:
            self.cmate=True
        elif len(kmoves)!=len(availKingMoves)\
            and\
            kplacesum>0:
            plroi.check=True
        elif kplacesum>0:
            plroi.check=True
        else:
            plroi.check=False
 
    def comparearr(self,pmoves,kmoves):
        ka=list()
        cntr=0
        for k in kmoves:
            for p in pmoves:
                if p!=k:
                    cntr+=1
            if cntr==len(pmoves):
                ka.append(k)
                cntr=0
        return ka

    def moveOk(self,pc,mv,chk):
        i=mv[0];j=mv[1]
        x=pc[0];y=pc[1]
        print("PC: "+str(pc))
        print("mv: "+str(mv))
        if self.board[x][y] is None:
            return False
        if chk==True:
            #pdb.set_trace()
            if 'King' not in str(self.board[x][y]):
                return False
        if (i>=0 and i <8) and (j>=0 and j <8):            
            if   (self.board[i][j] is None):
                return True
            elif ( self.board[x][y].player\
               !=self.board[i][j].player):
                return True
            else:
                return False
        else:
            return False

