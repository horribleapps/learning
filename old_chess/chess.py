from __future__ import print_function
import builtins as __builtin__
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pdb
#import checkmate as cm
from chesslib import *




def t_knight():
    #testing knight
    msk,brd,pm,bm=chessbrd()
    brd[lo+3][lo+2]='n11'
    brd[lo+0][lo+1]='000'
    pc='n11'
    plr=1
    brd,msk,pc,plr,pm,bm=nmask(brd,msk,pm,bm,pc,plr)
    disp(brd,bm,pm,msk)

def t_rook():
    #testing rook
    msk,brd,pm,bm=chessbrd()
    pc='r11'
    plr=1
    brd[lo+3][lo+2]='r11'
    brd[lo+0][lo+0]='000'
    brd[lo+0][lo+2]='000'
    brd[lo+3][lo+1]='b11'
    brd,pm=plrmat(brd,pm)
    #pdb.set_trace()
    brd,msk,pc,plr,pm,bm=rmask(brd,msk,pm,bm,pc,plr)
    disp(brd,bm,pm,msk)

def t_bishop():
    #testing bishop
    msk,brd,pm,bm=chessbrd()
    pc='b11'
    plr=1
    brd[lo+3][lo+2]='r11'
    brd[lo+0][lo+0]='000'
    brd[lo+0][lo+2]='000'
    brd[lo+4][lo+3]='b11'
    brd,pm=plrmat(brd,pm)
    brd,msk,pc,plr,pm,bm=bmask(brd,msk,pm,bm,pc,plr)
    disp(brd,bm,pm,msk)

def t_queen():
    #testing bishop
    msk,brd,pm,bm=chessbrd()
    pc='q11'
    plr=1
    brd[lo+3][lo+2]='r11'
    brd[lo+0][lo+0]='000'
    brd[lo+0][lo+3]='000'
    brd[lo+4][lo+3]='q11' 
    brd,pm=plrmat(brd,pm)
    disp(brd,bm,pm,msk) 
    brd,msk,pc,plr,pm,bm=qmask(brd,msk,pm,bm,pc,plr)
    disp(brd,bm,pm,msk)    

def t_king():
    #testing king
    msk,brd,pm,bm=chessbrd()
    pc='k11'
    plr=1
    brd[lo+3][lo+2]='r11'
    brd[lo+0][lo+0]='000'
    brd[lo+0][lo+4]='000'
    brd[lo+4][lo+3]='k11' 
    brd,pm=plrmat(brd,pm)
    disp(brd,bm,pm,msk) 
    brd,msk,pc,plr,pm,bm=kmask(brd,msk,pm,bm,pc,plr)
    disp(brd,bm,pm,msk) 

def t_pawn():
    #testing pawn
    msk,brd,pm,bm=chessbrd()
    pc='p12'
    plr=1
    brd[lo+3][lo+2]='p12'
    brd[lo+1][lo+2]='000'
    brd[lo+0][lo+4]='000'
    brd[lo+4][lo+3]='k11'
    brd[lo+4][lo+1]='p21'
    brd[lo+6][lo+1]='000'
    brd,pm=plrmat(brd,pm)
    brd,msk,pc,plr,pm,bm=pmask(brd,msk,pm,bm,pc,plr)
    disp(brd,bm,pm,msk) 

def dbgchk(mskdict,pmdict,brd,keyOI):
    print(brd[lo:hi,lo:hi])
    print()
    print(mskdict[keyOI][lo:hi,lo:hi].astype('int8'))
    print()
    print(pmdict[keyOI][lo:hi,lo:hi].astype('int8'))
    print()
    print(mskdict.keys())
    print()


def dbgchk(mskdict,pmdict,brd,keyOI):
    print(brd[lo:hi,lo:hi])
    print()
    print(mskdict[keyOI][lo:hi,lo:hi].astype('int8'))
    print()
    print(pmdict[keyOI][lo:hi,lo:hi].astype('int8'))
    print()
    print(mskdict.keys())
    print()
'''
def checkmate(brd,msk,pm,bm,pc,plr):
    print("inside checkmate")
    othplr = 2 if plr==1 else 1
    #x,y,pm,pc,brd,msk = updatebrd(msk,brd,pc,pm)
    othplpcs = brd[pm==othplr]
    disp(brd,bm,pm,msk)
    mskdict=dict()
    pmdict =dict()
    pcixy=np.where(brd==pc)
    brd[pcixy]='000'
    for pcoi in othplpcs:
        msk[:,:]=0
        pm[:,:]=0
        brd,pm=plrmat(brd,pm)
        tbrd,tmsk,tpc,tplr,tpm,bm=getmsk(brd,msk,pm,bm,pcoi,othplr)
        disp(brd,bm,pm,msk)   
        mskdict[pcoi]=tmsk.copy()
        pmdict[pcoi]=pm.copy()
        #print(mskdict['n22'][lo:hi,lo:hi].astype('int8'))
        #print(brd[lo:hi,lo:hi])
        #print(pmdict['n22'][lo:hi,lo:hi].astype('int8'))
        #print(mskdict.keys())
    otherplmsk=np.sum([x for x in mskdict.values()],axis=0).astype('bool') # combined mask of all othrplr pieces
    #print(otherplmsk[lo:hi,lo:hi].astype('int8'))
    msk[:,:]=0
    pm[:,:]=0
    #pdb.set_trace()
    brd[pcixy]=pc
    brd,pm=plrmat(brd,pm)
    #pdb.set_trace()
    brd,msk,pc,plr,pm,bm=kmask(brd,msk,pm,bm,pc,plr)
    #pdb.set_trace()
    print("\n\n")
    print("\npm")
    print(pm[lo:hi,lo:hi].astype('int8'))
    print("\notherplmsk")
    print(otherplmsk[lo:hi,lo:hi].astype('int8'))
    print("\nmsk")
    print(msk[lo:hi,lo:hi].astype('int8'))
    print("\ncheckmate msk")
    chmsk=~otherplmsk & msk
    print(chmsk[lo:hi,lo:hi].astype('int8'))
    print("\nbrd")
    print(brd[lo:hi,lo:hi])
    #pdb.set_trace()
    return brd,msk,pc,plr,pm,bm,chmsk

def checkmate2(brd,msk,pm,bm,pc,plr,chmsk):
    chblist=list()
    idx=0
    for ir,ic in zip(np.where(chmsk==True)[0],np.where(chmsk==True)[1]):
        tbrd=brd.copy();tmsk=msk.copy();tpm=pm.copy();tbm=bm.copy();tchmsk=chmsk.copy()
        tpc=pc;tplr=plr
        tmsk[:,:]=0
        tpm[:,:]=0
        tx,ty,tpm,tpc,tbrd,tmsk = updatebrd(tmsk,tbrd,tpc,tpm)
        tbrd[ir,ic]=tpc
        tbrd[tx,ty]='000'
        tbrd,tpm=plrmat(tbrd,tpm)
        tbrd,tmsk,tpc,tplr,tpm,tbm,tchmsk=checkmate(tbrd,tmsk,tpm,tbm,tpc,tplr)
        chblist.append(tchmsk)
    #pdb.set_trace()
    if np.sum(chblist)>0:
        return False
    else:
        return True
'''    


def t_checkmate_false():
    #testing pawn
    msk,brd,pm,bm=chessbrd()
    pc='k11'
    plr=1
    brd[lo+3][lo+2]='p12'
    brd[lo+1][lo+2]=\
    brd[lo+6][lo+5]=\
    brd[lo+7][lo+7]=\
    brd[lo+7][lo+0]=\
    '000'
    brd[lo+0][lo+4]='000'
    brd[lo+4][lo+3]='k11' # place king in middle
    brd[lo+4][lo+1]='p21' # 
    brd[lo+6][lo+5]='b22';brd[lo+7][lo+5]='p25'
    brd[lo+5][lo+0]='r21' #moving rook
    brd[lo+4][lo+6]='r22'
    brd[lo+6][lo+1]='000'
    tbrd,tpm=plrmat(brd,pm)
    brd,msk,pc,plr,pm,bm,chmsk=checkmate(brd,msk,pm,bm,pc,plr)
    chkbool=checkmate2(brd,msk,pm,bm,pc,plr,chmsk)
    disp(brd,bm,pm,msk)     
    print("Checkmate bool:"+str(chkbool))

def t_checkmate_true():
    #testing pawn
    msk,brd,pm,bm=chessbrd()
    pc='k11'
    plr=1
    brd[lo+3][lo+2]='p12'
    brd[lo+1][lo+2]=\
    brd[lo+6][lo+5]=\
    brd[lo+7][lo+7]=\
    brd[lo+7][lo+0]=\
    brd[lo+6][lo+3]=\
    brd[lo+7][lo+2]=\
    brd[lo+7][lo+6]=\
    '000'
    brd[lo+0][lo+4]='000'
    brd[lo+4][lo+3]='k11' # place king in middle
    #brd[lo+4][lo+3]='000'
    brd[lo+4][lo+1]='p21' # 
    brd[lo+6][lo+5]='b22';brd[lo+7][lo+5]='p25'
    brd[lo+3][lo+1]='b21'
    brd[lo+6][lo+1]='n22'
    brd[lo+5][lo+0]='r21' #moving rook
    brd[lo+4][lo+6]='r22'
    brd[lo+5][lo+5]='n22'
    brd,pm=plrmat(brd,pm)
    brd,msk,pc,plr,pm,bm,chmsk=checkmate(brd,msk,pm,bm,pc,plr)
    chkbool=checkmate2(brd,msk,pm,bm,pc,plr,chmsk)
    disp(brd,bm,pm,msk)     
    print("Checkmate bool:"+str(chkbool),force=True)



def main():
    global dbg
    if len(sys.argv)>1:
        if sys.argv[1]=='1':
            dbg=True
        else:
            dbg=False
    msk,brd,pm,bm=chessbrd()
    brd,pm=plrmat(brd,pm)
    chkbool=False
    idx=0
    while(~chkbool):
        #force=True;print(plr);force=False;
        if idx%2:
            plr=2
            brd,msk,pc,plr,pm,bm,chkbool=player(plr,msk,brd,pm,bm)
        else:
            plr=1
            brd,msk,pc,plr,pm,bm,chkbool=player(plr,msk,brd,pm,bm)
        msk[:,:] = 0
        #force=True;print(plr);force=False;
        #pm[:,:]  = 0
        #pdb.set_trace()
        idx+=1
        

    #t_knight()
    #t_rook()
    #t_bishop()
    #t_queen()
    #t_king()
    #t_pawn()
    #t_checkmate_false()
    #t_checkmate_true()



if __name__ == "__main__":
    main()

