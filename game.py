from __future__ import print_function
import builtins as __builtin__
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pdb
import random
import sys
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
            if (i>=0 and i <8) and (j>=0 and j <8):            
                if (gm.board[i][j] is not None) and\
                    (gm.board[i][j].player==plr):
                    gm.userPiece=gm.board[i][j]
                    gm.userx=i;gm.usery=j
                    breakInput=True
        except KeyboardInterrupt:
            sys.exit()
            continue 
        finally:
            print("This is not a valid piece")
            continue
    print("You have chosen: ")
    print(gm.userPiece)

def getUserxy(plr,gm,endTurn,moves,kingpc=None):
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
            if kingpc is None:
                gm.updateMove(tmplist,gm.userPiece)
                endTurn=True
            else:
                gm.updateMove(tmplist,kingpc)
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
        moves=gm.userPiece.availableMoves(gm.board)

def openTextFile(pn):
    strpn=str(pn)
    f=open('moves.txt','a')
    f.write(strpn+'\n')
    f.close()    

def main():
    '''#check
    moveslist={'1': [\
                    [[1,5],[2,5]],\
                    [[1,3],[2,3]],\
                    [[0,1],[2,0]],\
                    [[2,0],[0,1]],\
                    [[0,4],[1,3]],\
                    [[1,3],[2,4]],\
                    ],\

               '2': [\
                    [[6,4],[5,4]],\
                    [[7,1],[5,0]],\
                    [[7,3],[3,7]],\
                    [[3,7],[0,4]],
                    [[7,1],[5,0]],
                    ],\
               }'''

    #checkmate
    moveslist={'1':[[[1,5],[2,5]],[[0,1],[2,0]],[[2,0],[0,1]],],\
               '2':[[[6,4],[5,4]],[[7,5],[6,4]],[[6,4],[3,7]],],\
               }
    gm=Game()
    cm=False
    idx=0
    idx1=0;
    idx2=0;
    gm.printBoard()
    print("\n\n\n")
    while(gm.cmate==False):
    #for idx,(p1,p2) in enumerate(zip(moveslist['1'],moveslist['2'])):
        #pdb.set_trace()
        while(  (\
                (gm.etp1==False) \
                or \
                (gm.player1.check==True))\
                and\
                (gm.cmate==False)\
                ):
            p1=moveslist['1'][idx1]
            print('\n\nPlayer 1')
            pc=p1[0];mv=p1[1]
            openTextFile(1)
            movebool=gm.moveOk(pc,mv,gm.player1.check)
            if idx==2:
                x=1#pdb.set_trace()
            if movebool==True:
                gm.updateMove(mv,gm.board[pc[0]][pc[1]])
                gm.checkKing()
                gm.etp1=False if gm.player1.check==True else True
                #if gm.player1.check==True:
                #    x=1#pdb.set_trace()
                #if gm.player1.check==False:
                #    gm.etp1=True
            elif movebool==False:
                idx1+=1
            gm.printBoard()
            print("\n\n\n")
            #pdb.set_trace()
        gm.etp1=False
        idx1+=1
        while(  (\
                (gm.etp2==False) \
                or \
                (gm.player2.check==True))\
                and\
                (gm.cmate==False)\
                ):
            print('\n\nPlayer 2')
            p2=moveslist['2'][idx2]
            pc=p2[0];mv=p2[1]
            openTextFile(2)
            movebool=gm.moveOk(pc,mv,gm.player2.check)
            if idx>=2:
                x=1#pdb.set_trace
            if (movebool==True):
                gm.updateMove(mv,gm.board[pc[0]][pc[1]])
                gm.checkKing()
                gm.etp2=False if gm.player2.check==True else True
                #if gm.player2.check==False:
                #    gm.etp2=True
            elif movebool==False:
                idx2+=1
            gm.printBoard()
            print("\n\n\n")
            #if idx==2:
            #    pdb.set_trace()
        gm.etp2=False
        idx2+=1
        #pdb.set_trace()
    if gm.cmate==True:
        print("\n\nCheckmate!")

if __name__=="__main__":
    main()
