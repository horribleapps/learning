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
        self.check=False

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
        self.findKing(self.player1)
        self.findKing(self.player2)
    
    def findKing(self,plr):
        pmoves=list()
        #pdb.set_trace()
        for k in plr.pieces:
            pmoves.extend(\
            plr.pieces[k]\
            .availableMoves(self.board))
        #pdb.set_trace()
        if len(pmoves) > 0:
            idx=0
            for i,j in pmoves:
                if (self.board[i][j] is None):
                    idx+=1
                    continue
                if (self.board[i][j].player != plr.playerNumber)\
                    and \
                    (str(self.board[i][j])=='King'):
                    plr.check=True
                else:
                    idx+=1
            if len(plr.pieces)==idx:
                plr.check=True
            else:
                plr.check=False
        pdb.set_trace()
