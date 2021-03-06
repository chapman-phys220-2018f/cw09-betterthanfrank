#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name:Gabriella Nutt & Amelia & Gwenyth
#Student ID: 2307512
#Email: nutt@chapman.edu
#Course: PHYS220/MATH220/CPSC220 Fall 2018
#Assignment: CW09
###

import array_calculus as ac
import numpy as np

def test_gradient():
    """
    Tests that the gradient returns the correct values.
    """
    x = np.arange(0, 10,1)
    D = ac.gradient(x)
    D = D[:5]
    assert np.array_equal(D, np.array([[-1.,1.,0.,0.,0.,0.,0.,0.,0.,0.],[-0.5,0.,0.5,0.,0.,0.,0.,0.,0.,0.], [0.,-0.5,0.,0.5,0.,0.,0.,0.,0.,0.], [0.,0.,-0.5,0.,0.5,0.,0.,0.,0.,0.], [0.,0.,0.,-0.5,0.,0.5,0.,0.,0.,0.]]))