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
    print("pm cutdown")
    print(pm[lo:hi,lo:hi].astype('int8'))
    print("mask cutdown")
    print(msk[lo:hi,lo:hi].astype('int8'))

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

def updatebrd(msk,brd,pc,pm):
    msk[brd==pc]=True
    pm[brd==pc] =3 #setting current pc to 3
    ploc=np.where(brd==pc)#location of the piece
    x=ploc[0][0]
    y=ploc[1][0]  
    return x,y,pm,pc,brd,msk 

def nmask(brd,msk,pm,bm,pc,plr):
    '''
    brd: chess board
    msk: mask
    pc: chess piece of interest
    plr: player
    '''
    print("inside nmask")
    x,y,pm,pc,brd,msk =updatebrd(msk,brd,pc,pm)
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
    msk[(pm!=3)&(pm==plr)&(msk==True)]=False
    msk[~bm]=False# removing all things beyond the chess board
    #print(msk[lo:hi,lo:hi].astype('int8'))
    #print(pm[lo:hi,lo:hi].astype('int8'))
    brd,pm=plrmat(brd,pm)
    return brd,msk,pc,plr,pm,bm

def botpc(pm,p,msk,x,y,ogp):
    #below the pc
    b1=np.where(pm[x:,y] == p )[0]
    if len(b1) > 0 and ogp:
        b1=b1[0]+x+1
        msk[b1:,y]=False
    elif len(b1) > 0 and not ogp:
        b1=b1[0]+x
        msk[b1:,y]=False
    return msk

def abvpc(pm,p,msk,x,y,ogp):
    a1=np.where(pm[:x,y] == p )[0]
    if len(a1) > 0 and ogp:
        a1=a1[-1]
        msk[:a1,y]=False
    elif len(a1) > 0 and not ogp:
        a1=a1[-1]+1
        msk[:a1,y]=False
    return msk

def rgtpc(pm,p,msk,x,y,ogp):
    r1=np.where(pm[x,y:] == p )[0]
    if len(r1) > 0 and ogp:
        r1=r1[0]+y+1
        msk[x,r1:]=False
    elif len(r1) > 0 and not ogp:
        r1=r1[0]+y
        msk[x,r1:]=False
    return msk

def lftpc(pm,p,msk,x,y,ogp):
    l1=np.where(pm[x,:y] == p )[0]
    if len(l1) > 0 and ogp:
        l1=l1[-1]
        msk[x,:l1]=False
    elif len(l1) > 0 and not ogp:
        l1=l1[-1]+1
        msk[x,:l1]=False
    return msk

def rmask(brd,msk,pm,bm,pc,plr):
    '''
    brd: chess board
    msk: mask
    pc: chess piece of interest
    plr: player
    '''
    print("inside rmask")
    othplr = 2 if plr==1 else 1
    x,y,pm,pc,brd,msk = updatebrd(msk,brd,pc,pm)
    msk[x,:]=True
    msk[:,y]=True    
    #removing 2nd player parts
    #below the pc
    msk=botpc(pm,othplr,msk,x,y,True)
    #above the pc
    msk=abvpc(pm,othplr,msk,x,y,True)
    #right of pc
    msk=rgtpc(pm,othplr,msk,x,y,True)
    #left of pc
    msk=lftpc(pm,othplr,msk,x,y,True)
    #removing orig player parts
    #below the pc
    msk=botpc(pm,plr,msk,x,y,False)
    #above the pc
    msk=abvpc(pm,plr,msk,x,y,False)
    #right of pc
    msk=rgtpc(pm,plr,msk,x,y,False)
    #left of pc
    msk=lftpc(pm,plr,msk,x,y,False)
    msk[~bm]=False
    brd,pm=plrmat(brd,pm)
    disp(brd,bm,pm,msk)
    return brd,msk,pc,plr,pm,bm

def brpc(pm,p,msk,x,y,ogp):
    row,col=np.diag_indices_from(msk[x:x+8,y:y+8])
    msk[x+row,y+col]=True
    br1 = np.where(pm[x+row,y+col]==p)[0]
    if len(br1) > 0 and ogp:
        br1=br1[0]
        msk[ x+row[br1:],y+col[br1:] ] = False
    elif len(br1) > 0 and not ogp:
        br1=br1[0]+1
        msk[ x+row[br1:],y+col[br1:] ] = False
    return msk

def tlpc(pm,p,msk,x,y,ogp):
    row,col=np.diag_indices_from(msk[x-8:x,y-8:y])
    msk[x-8+row,y-8+col]=True
    lt1 = np.where(pm[x-8+row,y-8+col])[0]
    if len(lt1) > 0 and ogp:
        lt1=lt1[-1]
        msk[ x-8+row[:lt1], y-8+col[:lt1] ] = False
    elif len(lt1) > 0 and not ogp:
        lt1=lt1[-1]+1
        msk[ x-8+row[:lt1], y-8+col[:lt1] ] = False
    return msk

def flipmat(msk,pm,bm,brd):
    brd= np.fliplr(brd)
    msk= np.fliplr(msk)
    pm = np.fliplr(pm)
    bm = np.fliplr(bm)
    return brd,msk,pm,bm

def diagmskupdate(pm,othplr,msk,x,y):
    msk=brpc(pm,othplr,msk,x,y,True)
    msk=tlpc(pm,othplr,msk,x,y,True)
    #for the original player
    msk=brpc(pm,othplr,msk,x,y,False)
    msk=tlpc(pm,othplr,msk,x,y,False)
    return msk,pm,othplr,msk,x,y

def bmask(brd,msk,pm,bm,pc,plr):
    print("inside bmask")
    #print(msk[lo:hi,lo:hi].astype('int8'))
    othplr = 2 if plr==1 else 1
    x,y,pm,pc,brd,msk = updatebrd(msk,brd,pc,pm)
    msk,pm,othplr,msk,x,y=diagmskupdate(pm,othplr,msk,x,y)

    #flip mat
    brd,msk,pm,bm=flipmat(msk,pm,bm,brd)
    #flip mats left to right to get tr to work
    othplr = 2 if plr==1 else 1
    x,y,pm,pc,brd,msk = updatebrd(msk,brd,pc,pm)
    msk,pm,othplr,msk,x,y=diagmskupdate(pm,othplr,msk,x,y)

    #flip mats back
    brd,msk,pm,bm=flipmat(msk,pm,bm,brd)
    msk[~bm]=False
    brd,pm=plrmat(brd,pm)
    disp(brd,bm,pm,msk)
    return brd,msk,pc,plr,pm,bm

def qmask(brd,msk,pm,bm,pc,plr):
    print("inside queen")
    brd,msk,pc,plr,pm,bm = bmask(brd,msk,pm,bm,pc,plr)
    disp(brd,bm,pm,msk)
    brd,msk,pc,plr,pm,bm = rmask(brd,msk,pm,bm,pc,plr)
    msk[~bm]=False
    brd,pm=plrmat(brd,pm)
    disp(brd,bm,pm,msk)
    return brd,msk,pc,plr,pm,bm

def kmask(brd,msk,pm,bm,pc,plr):
    print("inside rmask")
    othplr = 2 if plr==1 else 1
    x,y,pm,pc,brd,msk = updatebrd(msk,brd,pc,pm)
    msk[x-1:x+2,y-1:y+2]=True
    msk[x-1:x+2,y-1:y+2][ pm[x-1:x+2,y-1:y+2]==plr ] = False
    msk[~bm]=False
    brd,pm=plrmat(brd,pm)
    disp(brd,bm,pm,msk)
    return brd,msk,pc,plr,pm,bm

def pmask(brd,msk,pm,bm,pc,plr):
    print("inside pmask")
    othplr = 2 if plr==1 else 1
    x,y,pm,pc,brd,msk = updatebrd(msk,brd,pc,pm)
    if plr==1:
        msk[x+1,y] = True if pm[x+1,y]==0 else False
        if pm[x+1,y+1]==othplr:
            msk[x+1,y+1]=True
        if pm[x+1,y-1]==othplr:
            msk[x+1,y-1]=True

    elif plr==2:
        #msk[x-1,y][pm[x-1,y]==0]=True
        msk[x-1,y] = True if pm[x-1,y]==0 else False
        if pm[x-1,y+1]==othplr:
            msk[x-1,y+1]=True
        if pm[x-1,y-1]==othplr:
            msk[x-1,y-1]=True
    #pdb.set_trace()
    msk[~bm]=False
    brd,pm=plrmat(brd,pm)
    disp(brd,bm,pm,msk)
    return brd,msk,pc,plr,pm,bm

def getmsk(brd,msk,pm,bm,pc,plr):
    if 'r' in pc[0]:
        brd,msk,pc,plr,pm,bm=rmask(brd,msk,pm,bm,pc,plr)
    elif 'n' in pc[0]:
        brd,msk,pc,plr,pm,bm=nmask(brd,msk,pm,bm,pc,plr)
    elif 'b' in pc[0]:
        brd,msk,pc,plr,pm,bm=bmask(brd,msk,pm,bm,pc,plr)
    elif 'q' in pc[0]:
        brd,msk,pc,plr,pm,bm=qmask(brd,msk,pm,bm,pc,plr)
    elif 'k' in pc[0]:
        brd,msk,pc,plr,pm,bm=kmask(brd,msk,pm,bm,pc,plr)
    elif 'p' in pc[0]:
        brd,msk,pc,plr,pm,bm=pmask(brd,msk,pm,bm,pc,plr)
    return brd,msk,pc,plr,pm,bm

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


def checkmate(brd,msk,pm,bm,pc,plr):
    print("inside checkmate")
    othplr = 2 if plr==1 else 1
    #x,y,pm,pc,brd,msk = updatebrd(msk,brd,pc,pm)
    othplpcs = brd[pm==othplr]
    disp(brd,bm,pm,msk)
    mskdict=dict()
    pmdict =dict()
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
    msk[:,:]=0
    pm[:,:]=0
    brd,pm=plrmat(brd,pm)
    brd,msk,pc,plr,pm,bm=kmask(brd,msk,pm,bm,pc,plr)
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
    pdb.set_trace()
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
    brd,pm=plrmat(brd,pm)
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
    print("Checkmate bool:"+str(chkbool))



def main():
    if len(sys.argv)>1:
        if sys.argv[1]=='1':
            dbg=True
        else:
            dbg=False
    #t_knight()
    #t_rook()
    #t_bishop()
    #t_queen()
    #t_king()
    #t_pawn()
    #t_checkmate_false()
    t_checkmate_true()


if __name__ == "__main__":
    main()

