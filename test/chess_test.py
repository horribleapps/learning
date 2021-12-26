import sys
sys.path.insert(1, '/home/archie/git-repos/learning')
import pytest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pdb
from chess import *



def test_nmask():
    #testing knight
    msk,brd,pm,bm=chessbrd()
    brd[lo+3][lo+2]='n11'
    brd[lo+0][lo+1]='000'
    pc='n11'
    plr=1
    brd,msk,pc,plr,pm,bm=nmask(brd,msk,pm,bm,pc,plr)
    brd,pm=plrmat(brd,pm)
    disp(brd,bm,pm,msk)
    msktest=\
    np.array([\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [1, 0, 0, 0, 1, 0, 0, 0,],\
                [0, 0, 1, 0, 0, 0, 0, 0,],\
                [1, 0, 0, 0, 1, 0, 0, 0,],\
                [0, 1, 0, 1, 0, 0, 0, 0,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
            ])
    pmtest=\
    np.array([\
                [1, 0, 1, 1, 1, 1, 1, 1,],\
                [1, 1, 1, 1, 1, 1, 1, 1,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [0, 0, 1, 0, 0, 0, 0, 0,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [2, 2, 2, 2, 2, 2, 2, 2,],\
                [2, 2, 2, 2, 2, 2, 2, 2,],\
    ])
    assert np.sum(~(msk[lo:hi,lo:hi]==msktest))+\
            np.sum(~(pm[lo:hi,lo:hi]==pmtest))==0, "masks don't match"


def test_rmask():
    msk,brd,pm,bm=chessbrd()
    pc='r11'
    plr=1
    brd[lo+3][lo+2]='r11'
    brd[lo+0][lo+0]='000'
    brd[lo+0][lo+2]='000'
    brd[lo+3][lo+1]='b11'
    brd,pm=plrmat(brd,pm)
    brd,msk,pc,plr,pm,bm=rmask(brd,msk,pm,bm,pc,plr)
    brd,pm=plrmat(brd,pm)
    disp(brd,bm,pm,msk)
    msktest=\
    np.array([\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [0, 0, 1, 0, 0, 0, 0, 0,],\
                [0, 0, 1, 1, 1, 1, 1, 1,],\
                [0, 0, 1, 0, 0, 0, 0, 0,],\
                [0, 0, 1, 0, 0, 0, 0, 0,],\
                [0, 0, 1, 0, 0, 0, 0, 0,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
            ])
    pmtest=\
    np.array([\
                [0, 1, 0, 1, 1, 1, 1, 1,],\
                [1, 1, 1, 1, 1, 1, 1, 1,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [0, 1, 1, 0, 0, 0, 0, 0,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [2, 2, 2, 2, 2, 2, 2, 2,],\
                [2, 2, 2, 2, 2, 2, 2, 2,],\
    ])
    assert np.sum(~(msk[lo:hi,lo:hi]==msktest))+\
            np.sum(~(pm[lo:hi,lo:hi]==pmtest))==0, "masks don't match"


def test_bmask():
    msk,brd,pm,bm=chessbrd()
    pc='b11'
    plr=1
    brd[lo+3][lo+2]='r11'
    brd[lo+0][lo+0]='000'
    brd[lo+0][lo+2]='000'
    brd[lo+4][lo+3]='b11'
    brd,pm=plrmat(brd,pm)
    brd,msk,pc,plr,pm,bm=bmask(brd,msk,pm,bm,pc,plr)
    brd,pm=plrmat(brd,pm)
    disp(brd,bm,pm,msk)
    msktest=\
    np.array([\
                [0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 1, 0, 0,],
                [0, 0, 0, 0, 1, 0, 0, 0,],
                [0, 0, 0, 1, 0, 0, 0, 0,],
                [0, 0, 1, 0, 1, 0, 0, 0,],
                [0, 1, 0, 0, 0, 1, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0,],
            ])
    pmtest=\
    np.array([\
                [0, 1, 0, 1, 1, 1, 1, 1,],\
                [1, 1, 1, 1, 1, 1, 1, 1,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [0, 0, 1, 0, 0, 0, 0, 0,],\
                [0, 0, 0, 1, 0, 0, 0, 0,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [2, 2, 2, 2, 2, 2, 2, 2,],\
                [2, 2, 2, 2, 2, 2, 2, 2,],\
    ])
    assert np.sum(~(msk[lo:hi,lo:hi]==msktest))+\
            np.sum(~(pm[lo:hi,lo:hi]==pmtest))==0, "masks don't match"


def test_qmask():
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
    brd,pm=plrmat(brd,pm)
    disp(brd,bm,pm,msk)   
    msktest=\
    np.array([\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [0, 0, 0, 1, 0, 1, 0, 0,],\
                [0, 0, 0, 1, 1, 0, 0, 0,],\
                [1, 1, 1, 1, 1, 1, 1, 1,],\
                [0, 0, 1, 1, 1, 0, 0, 0,],\
                [0, 1, 0, 1, 0, 1, 0, 0,],\
                [0, 0 ,0, 0, 0, 0, 0, 0,],\
            ])
    pmtest=\
    np.array([\
                [0, 1, 1, 0, 1, 1, 1, 1,],\
                [1, 1, 1, 1, 1, 1, 1, 1,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [0, 0, 1, 0, 0, 0, 0, 0,],\
                [0, 0, 0, 1, 0, 0, 0, 0,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [2, 2, 2, 2, 2, 2, 2, 2,],\
                [2, 2, 2, 2, 2, 2, 2, 2,],\
    ])
    assert np.sum(~(msk[lo:hi,lo:hi]==msktest))+\
            np.sum(~(pm[lo:hi,lo:hi]==pmtest))==0, "masks don't match"


def test_kmask():
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
    brd,pm=plrmat(brd,pm)
    disp(brd,bm,pm,msk)    
    msktest=\
    np.array([\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [0, 0, 0, 1, 1, 0, 0, 0,],\
                [0, 0, 1, 1, 1, 0, 0, 0,],\
                [0, 0, 1, 1, 1, 0, 0, 0,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
            ])
    pmtest=\
    np.array([\
                [0, 1, 1, 1, 0, 1, 1, 1,],\
                [1, 1, 1, 1, 1, 1, 1, 1,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [0, 0, 1, 0, 0, 0, 0, 0,],\
                [0, 0, 0, 1, 0, 0, 0, 0,],\
                [0, 0, 0, 0, 0, 0, 0, 0,],\
                [2, 2, 2, 2, 2, 2, 2, 2,],\
                [2, 2, 2, 2, 2, 2, 2, 2,],\
    ])
    assert np.sum(~(msk[lo:hi,lo:hi]==msktest))+\
            np.sum(~(pm[lo:hi,lo:hi]==pmtest))==0, "masks don't match"

