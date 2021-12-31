from __future__ import print_function
import builtins as __builtin__
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import pdb
from chess import *


def test_chess():
    gm=Game()
    rk=gm.board[0][7]
    print(rk.availableMoves())