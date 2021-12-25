from __future__ import print_function
import builtins as __builtin__
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pdb


dbg=True
lo=8
hi=16
length=24

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

def initpcs(brd):
    global lo
    global hi
    #rook
    brd[0+lo][0+lo]='r11'
    brd[0+lo][hi-1]='r12'
    brd[hi-1][0+lo]='r21'
    brd[hi-1][hi-1]='r22'
    #knight
    brd[0+lo][1+lo]='n11'
    brd[0+lo][hi-2]='n12'
    brd[hi-1][1+lo]='n21'
    brd[hi-1][hi-2]='n22'
    #bishop
    #brd[3][2]='b11'
    brd[0+lo][2+lo]='b11'
    brd[0+lo][hi-3]='b12'
    brd[hi-1][2+lo]='b21'
    brd[hi-1][hi-3]='b22'
    #queen/king
    brd[0+lo][3+lo]='q11'
    brd[0+lo][hi-4]='k12'
    brd[hi-1][3+lo]='q21'
    brd[hi-1][hi-4]='k22'
    #empty cells are reset to empty strings
    brd[brd=='0.0']='000'
    #create pawns
    for idx,x in enumerate([1+lo,hi-2]):
        for j in np.arange(lo,hi):
            brd[x,j]='p'+str(np.abs(idx+1))+str(j-lo)
    print(brd[lo:hi,lo:hi])
    return brd

def plrmat(brd,pm):
    global length
    vfunc=np.vectorize(lambda a: int(a[1]))
    pm=vfunc(brd)
    return brd,pm

def disp(brd,bm,pm,msk):
    print("msk")
    print(msk.astype('int8'))
    print("brd")
    print(brd)
    print("pm")
    print(pm)
    print("bm")
    print(bm.astype('int8'))
    print("chess board")
    print(brd[lo:hi,lo:hi])

def chessbrd():
    global dbg
    global hi
    global lo
    msk =np.zeros((24,24)).astype('bool')
    brd =np.zeros((24,24)).astype('str')
    pm  =np.zeros((24,24)).astype('int8')
    bm  =np.zeros((24,24)).astype('bool')
    brd =initpcs(brd)
    #create border matrix
    bm[0:8,0:24]  =False
    bm[16:,16:]   =False
    bm[16:,0:24]  =False
    bm[8:16,8:16] =True
    brd,pm = plrmat(brd,pm)
    disp(brd,bm,pm,msk)
    return msk,brd,pm,bm

def nmask(brd,msk,pm,bm,pc,plr):
    '''
    brd: chess board
    msk: mask
    pc: chess piece of interest
    plr: player
    '''
    print("inside nmask")

    msk[brd==pc]=True
    ploc=np.where(brd==pc)#location of the piece
    x=ploc[0][0]
    y=ploc[1][0]
    print((x-lo,y-lo))
    # where knight can go
    msk[x+2,y+1]=True
    msk[x-2,y-1]=True
    msk[x-2,y+1]=True
    msk[x+2,y-1]=True
    msk[x+1,y+2]=True
    msk[x-1,y-2]=True
    msk[x-1,y+2]=True
    msk[x+1,y-2]=True
    #removing pcs from the same player
    
    msk[~bm]=False# removing all things beyond the chess board
    print(msk[lo:hi,lo:hi].astype('int8'))
    pdb.set_trace()
    return brd,msk,pc,plr,pm,bm
    '''
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
    '''

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
    x=ploc[0][0]
    y=ploc[1][0]
    msk[x,:]=True
    msk[:,y]=True
    msk=updatemsk(brd,msk,pc,plr)
    trck=-1
    
    if x+1<8:
        for i in np.arange(x+1,np.shape(msk)[1]):
            tmp=brd[i,y]
            if ((tmp[1] not in plr) and (trck==-1) and (tmp not in '000')):
                trck=i 
            elif (tmp[1] not in plr) and (i>trck) and (tmp not in '000'):
                msk[i,y]=False
    elif x-1>-1:
        for i in np.arange(x-1,0):
            tmp=brd[i,y]
            if ((tmp[1] not in plr) and (trck==-1) and (tmp not in '000')):
                trck=i 
            elif (tmp[1] not in plr) and (i<trck) and (tmp not in '000'):
                msk[i,y]=False
    if y+1<8:
        for i in np.arange(y+1,np.shape(msk)[1]):
            tmp=brd[x,i]
            if ((tmp[1] not in plr) and (trck==-1) and (tmp not in '000')):
                trck=i 
            elif (tmp[1] not in plr) and (i>trck) and (tmp not in '000'):
                msk[x,i]=False
    elif y-1>-1:
        for i in np.arange(y-1,0):
            tmp=brd[x,i]
            if ((tmp[1] not in plr) and (trck==-1) and (tmp not in '000')):
                trck=i 
            elif (tmp[1] not in plr) and (i<trck) and (tmp not in '000'):
                msk[x,i]=False
    #pdb.set_trace()
    #msk[ np.where(msk[x,:]==False)[0][0]:,: ]=False
    #msk[ np.where(msk[:,y]==False)[0][0] ]=False
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

def main():
    if len(sys.argv)>1:
        if sys.argv[1]=='1':
            dbg=True
        else:
            dbg=False
    msk,brd,pm,bm=chessbrd()
    brd[lo+3][lo+2]='n11'
    brd[lo+0][lo+1]='000'
    pc='n11'
    plr=1
    brd,msk,pc,plr,pm,bm=nmask(brd,msk,pm,bm,pc,plr)
    pdb.set_trace()
    '''
    brd,msk=chessbrd()
    brd[3][2]='b11'
    brd[0][2]='000'
    pc='n11'
    plr='1'
    brd,msk,pc,plr=nmask(brd,msk,pc,plr)
    '''
    '''
    #testing rook
    brd,msk=chessbrd()
    brd[3][2]='r11'
    brd[0][0]='000'
    brd[0][2]='000'
    brd[3][1]='b11'
    pc='r11'
    plr='1'
    brd,msk,pc,plr=rmask(brd,msk,pc,plr)
    '''


if __name__ == "__main__":
    main()

