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
    e = ((f*(x+dx)-f*(x-dx))/(2*dx))
    x = np.linspace([n])
    a = np.dia(np.ones_like(x[:-1]),k =1 )#imputs 1D Array and Outputs 2D look up manipulation
    b = np.diag(np.ones_like(x[:-1]),k =-1 )
    D = (1/(2*dx))(a+b)
    
