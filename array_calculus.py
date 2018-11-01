#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name:Gabriella Nutt
#Student ID: 2307512
#Email: nutt@chapman.edu
#Course: PHYS220/MATH220/CPSC220 Fall 2018
#Assignment: Midterm
###

import numpy as np
import seaborn as sb
import pandas as pd

def gradient(x):
    """"""
    dx = x[1]-x[0]
    N = len(x)
    x = np.linspace(-10,10, num = 100, endpoint = True)
    a = np.diag(np.ones_like(x[:-1]),k =1 )#imputs 1D Array and Outputs 2D look up manipulation
    b = np.diag(np.ones_like(x[:-1]),k =-1 )
    m = (a+b)
    m[0][2]=2
    m[0][0:1] = [-2:2]
    D = (1/(2*dx))(m)
    return D

fp= D @ f
