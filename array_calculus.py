#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name:Gabriella Nutt
#Student ID: 2307512
#Email: nutt@chapman.edu
#Course: PHYS220/MATH220/CPSC220 Fall 2018
#Assignment: CW09
###

import numpy as np
import matplotlib.pyplot as plt

def gradient(x):
    """This function creates the gradient matrix. The first two elements of the first row are -2 and 2 and the remaining elements are zeros. The last two elements of         the very last row are -2 and 2 while the other elements are all zeros. The main diagonal is made up of all zeros while the diagonal below it is made up of           all -1's and the diagonal above it is all 1's. That whole matrix is divided by 2dx."""
    dx = x[1]-x[0]
    N = len(x)
    a = np.diag(np.ones_like(x[:-1]),k =1 )#imputs 1D Array and Outputs 2D look up manipulation
    b = np.diag(np.ones_like(x[:-1]),k =-1 )
    m = (a+b)
    m[0][2]=2
    m[0][0:2] = [-2,2]
    D = ((m)/2*dx)
    return D

def xsquared():
    "this plots the function x^2 yay"
    
    fx = x**2
    x = np.linspace(-10,10, num = 100, endpoint = True)
    fdx = D @ fx
    
    plt.plot(fx,color="k")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot of x^2')
    plt.ylim((0,100)) #stackoverflow
    plt.show()


