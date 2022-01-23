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
            pdb.set_trace()
            moveDone=True
            gm.kingInCheck(poi,gm.board)
            pdb.set_trace()
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

def main():
    gm=Game()
    cm=False
    idx=0;
    while(~gm.cmate):
        if idx%2==0:
            f=open('moves.txt','a')
            f.write('1\n')
            f.close()
            pickMove(1,gm)
        else:
            f=open('moves.txt','a')
            f.write('2\n')
            f.close()
            pickMove(2,gm)
        idx+=1


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