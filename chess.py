from __future__ import print_function
import builtins as __builtin__
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pdb


dbg=True

def print(*args, force=False,**kwargs,):
    """My custom print() function."""
    # Adding new arguments to the print function signature 
    # is probably a bad idea.
    # Instead consider testing if custom argument keywords
    # are present in kwargs
    global dbg
    if dbg or force:
        __builtin__.print(*args,**kwargs)
    else:
        k=1
    #return __builtin__.print(*args, **kwargs)

def chessbrd():
    global dbg
    msk=np.zeros((8,8)).astype('bool')
    brd=np.zeros((8,8)).astype('str')
    #rook
    brd[0][0]='r11'
    brd[0][-1]='r12'
    brd[-1][0]='r21'
    brd[-1][-1]='r22'
    #knight
    brd[0][1]='n11'
    brd[0][-2]='n12'
    brd[-1][1]='n21'
    brd[-1][-2]='n22'
    #bishop
    brd[0][2]='b11'
    brd[0][-3]='b12'
    brd[-1][2]='b21'
    brd[-1][-3]='b22'
    #queen/king
    brd[0][3]='q11'
    brd[0][-4]='k12'
    brd[-1][3]='q21'
    brd[-1][-4]='k22'
    #empty cells are reset to empty strings
    brd[brd=='0.0']='000'
    #create pawns
    for x in [1,-2]:
        for j in np.arange(np.shape(brd)[1]):
            brd[x,j]='p'+str(np.abs(x))+str(j)
    print("msk")
    print(msk)
    print("brd")
    print(brd)

    return brd,msk

def nmask(brd,msk,pc,plr):
    '''
    brd: chess board
    msk: mask
    pc: chess piece of interest
    plr: player
    '''
    print("inside nmask")
    msk[brd==pc]=True
    ploc=np.where(brd==pc)#location of the piece
    ploc=[ploc[0][0],ploc[1][0]]
    # where knight can go
    llist=  [\
            [ploc[0]+2,ploc[1]+1],\
            [ploc[0]-2,ploc[1]-1],\
            [ploc[0]-2,ploc[1]+1],\
            [ploc[0]+2,ploc[1]-1],\

            [ploc[0]+1,ploc[1]+2],\
            [ploc[0]-1,ploc[1]-2],\
            [ploc[0]-1,ploc[1]+2],\
            [ploc[0]+1,ploc[1]-2],\
            ]
    print(llist)
    llist=[[x,y] for x,y in llist if ((x>=0 and x<9) and (y>=0 and y<8))]#list of all locations that are not beyond the board
    #this ignores if there is a piece in the way or not
    print(llist)
    xlist=[h[0] for h in llist]
    ylist=[h[1] for h in llist]
    print(xlist)
    print(ylist)
    msk[xlist,ylist]=True
    print(msk.astype('int8'))
    msk=updatemsk(brd,msk,pc,plr)
    return brd,msk,pc,plr

def rmask(brd,msk,pc,plr):
    '''
    brd: chess board
    msk: mask
    pc: chess piece of interest
    plr: player
    '''
    print(rmask)
    msk[:,:]=False
    msk[brd==pc]=True
    ploc=np.where(brd==pc)#location of the piece
    msk[ploc[0][0],:]=True
    msk[:,ploc[1][0]]=True
    msk=updatemsk(brd,msk,pc,plr)
    
    return brd,msk,pc,plr


def updatemsk(brd,msk,pc,plr):
    print("inside update msk")
    othplr='2' if plr=='1' else '1'
    temp=np.zeros((8,8)).astype('bool')
    temp[brd=='000']=True
    temp[brd!='000']=False
    temp[brd==pc]=True
    othplrlist=[s for s in brd[msk] if s[1]==othplr]
    msk=msk&temp
    print('msk b4 player compensation')
    print(msk.astype('int8'))
    othplrloc=[np.where(brd==oth) for oth in othplrlist]
    xlist=[h[0] for h in othplrloc]
    ylist=[h[1] for h in othplrloc]
    msk[xlist,ylist]=True
    print('msk after player compensation')
    print(msk.astype('int8'))
    return msk


if len(sys.argv)>1:
    if sys.argv[1]=='1':
        dbg=True
    else:
        dbg=False
brd,msk=chessbrd()
pc='n11'
plr='1'
brd,msk,pc,plr=nmask(brd,msk,pc,plr)

#testing rook
brd,msk=chessbrd()
pc='r11'
plr='1'
brd,msk,pc,plr=rmask(brd,msk,pc,plr)

