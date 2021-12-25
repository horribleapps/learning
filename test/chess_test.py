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
    brd,msk=chessbrd()
    brd[3][2]='b11'
    brd[0][2]='000'
    msktest=\
    np.array([[False,  True, False, False, False, False, False, False],\
        [False, False, False, False, False, False, False, False],\
        [ True, False,  True, False, False, False, False, False],\
        [False, False, False, False, False, False, False, False],\
        [False, False, False, False, False, False, False, False],\
        [False, False, False, False, False, False, False, False],\
        [False, False, False, False, False, False, False, False],\
        [False, False, False, False, False, False, False, False]])    
    pc='n11'
    plr='1'
    brd,msk,pc,plr=nmask(brd,msk,pc,plr)
    assert np.sum(~(msk==msktest))==0

def test_nmask():
    brd,msk=chessbrd()
    brd[3][2]='b11'
    brd[0][2]='000'
    msktest=\
    np.array([\
            [False,  True, False, False, False, False, False, False],\
            [False, False, False, False, False, False, False, False],\
            [ True, False,  True, False, False, False, False, False],\
            [False, False, False, False, False, False, False, False],\
            [False, False, False, False, False, False, False, False],\
            [False, False, False, False, False, False, False, False],\
            [False, False, False, False, False, False, False, False],\
            [False, False, False, False, False, False, False, False]\
            ])    
    pc='n11'
    plr='1'
    brd,msk,pc,plr=nmask(brd,msk,pc,plr)
    assert np.sum(~(msk==msktest))==0

def test_nmask():
    brd,msk=chessbrd()
    brd[3][2]='b11'
    brd[0][2]='000'
    msktest=\
    np.array([\
        [ True, False,  True, False, False, False, False, False],\
        [False, False, False, False, False, False, False, False],\
        [ True, False, False, False, False, False, False, False],\
        [ True, False, False, False, False, False, False, False],\
        [ True, False, False, False, False, False, False, False],\
        [ True, False, False, False, False, False, False, False],\
        [ True, False, False, False, False, False, False, False],\
        [ True, False, False, False, False, False, False, False]\
        ])
    pc='n11'
    plr='1'
    brd,msk,pc,plr=rmask(brd,msk,pc,plr)
    assert np.sum(~(msk==msktest))==0


