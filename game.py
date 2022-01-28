from __future__ import print_function
import builtins as __builtin__
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pdb
import random
from chess import Game
from piece import *


def pickMove(plr,gm):
    plist=list()
    for i in range(gm.uplim+1):
        for j in range(gm.uplim+1):
            tmp=gm.board[i][j]
            if tmp is not None:
                if tmp.player==plr:
                    plist.append(tmp)
    #pdb.set_trace()
    moveDone=False
    while(not moveDone or not gm.cmate):
        poi=random.choice(plist)
        print(poi,end=" ")
        print(poi.player,end=" ")
        print()
        #pdb.set_trace()
        moves=poi.availableMoves(gm.board)
        if poi.seeKing == True:
            #pdb.set_trace()
            moveDone=True
            gm.kingInCheck(poi,gm.board)
            #pdb.set_trace()
            break
        #pdb.set_trace()
        if len(moves) > 0:
            pcloc=random.choice(moves)
            gm.updateMove(pcloc,poi)
            moveDone=True
            break
        elif len(moves) == 1:
            pcloc=moves
            gm.updateMove(pcloc,poi)
            moveDone=True
            break
        else:
            continue

def getPiece(plr,gm):
    breakInput=False
    print("Player: "+str(plr))
    while(not breakInput):
        try:
            playerPieceInput=input("Please put location of the piece\n")
            i=int(playerPieceInput[0])
            j=int(playerPieceInput[2])
            if (i>=0 and i <8) and (i>=0 and i <8):            
                if (gm.board[i][j] is not None) and\
                    (gm.board[i][j].player==plr):
                    gm.userPiece=gm.board[i][j]
                    gm.userx=i;gm.usery=j
                    breakInput=True
        except:
            print("This is not a valid piece")
            continue
    print("You have chosen: ")
    print(gm.userPiece)

def getUserxy(plr,gm,endTurn,moves):
    breakInput=False
    print("Available moves:")
    print(moves)
    while(not breakInput):
        playerMove=input("Put move\n")
        if len(playerMove)==0:
            continue
        tmplist=[int(playerMove[0]),int(playerMove[2])]
        boolList=list()
        for x in moves:
            if x==tmplist:
                boolList.append(True)
            else:
                boolList.append(False)
        if sum(boolList)==0:
            print("That move is not available!\n")
        else:
            gm.updateMove(tmplist,gm.userPiece)
            endTurn=True
            break
    return endTurn


def userMove(plr,gm):
    gm.printBoard()
    gm.userPiece=None
    gm.userx=-1
    gm.usery=-1
    endTurn=False
    while(not endTurn):
        getPiece(plr,gm)
        moves=gm.userPiece.availableMoves(gm.board)
        if len(moves)==0:
            print("This piece can't move anywhere")
            continue
        breakInput=False
        print("Available moves:")
        print(moves)
        endTurn=getUserxy(plr,gm,endTurn,moves)


def main():
    gm=Game()
    cm=False
    idx=0
    while((~gm.cmate) and (~gm.stalemate)):
        if idx%2==0:
            f=open('moves.txt','a')
            f.write('1\n')
            f.close()
            userMove(1,gm)
            #pickMove(1,gm)
        else:
            f=open('moves.txt','a')
            f.write('2\n')
            f.close()
            userMove(2,gm)
            #pickMove(2,gm)
        idx+=1
    if gm.cmate:
        print("Game over!")


if __name__=="__main__":
    main()

'''
rk=gm.board[0][7]
hh=rk.availableMoves(gm.board)
print(len(hh))
bh = gm.board[0][2]
bb=bh.availableMoves(gm.board)
print(len(bb))
gm.updateMove([4,4],bh)
qu = gm.board[0][3]
qq=qu.availableMoves(gm.board)
pdb.set_trace()
'''