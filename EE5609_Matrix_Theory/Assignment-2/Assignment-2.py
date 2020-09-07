# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 08:44:47 2020

Course: EE5609 Matrix Theory (Assignment-2)

@author: kranthi Kumar P
"""

import numpy as np
#import matplotlib.pyplot as plt

# Function for shortest distance of a plane from point P
def DistancefromPlane(coeff,aug,P):
    # Input Arguments
    # coeff - Coefficients of linear equation
    # aug - augment of linear equation
    # P - point from where the disance as to be calculated
    normal = coeff
    Q = np.array([0.0, 0.0, 0.0])
    for i,val in enumerate(normal):
        if val != 0:
            Q[i] = aug/val
            break
    distance = np.abs(np.dot(np.subtract(Q,P),normal.T)/np.linalg.norm(normal))
    return distance

# Problem (a)
A = np.array([0,0,1])
aug = 2
P = np.array([0,0,0])
dist = DistancefromPlane(A,aug,P)
print("Shortest Distance of Plane from Origin is {0}".format(dist))

# Problem (b)
A = np.array([1,1,1])
aug = 1
P = np.array([0,0,0])
dist = DistancefromPlane(A,aug,P)
print("Shortest Distance of Plane from Origin is {0}".format(dist))

# Problem (c)
A = np.array([0,5,0])
aug = -8
P = np.array([0,0,0])
dist = DistancefromPlane(A,aug,P)
print("Shortest Distance of Plane from Origin is {0}".format(dist))

# Problem (d)
A = np.array([2,3,-1])
aug = 5
P = np.array([0,0,0])
dist = DistancefromPlane(A,aug,P)
print("Shortest Distance of Plane from Origin is {0}".format(dist))
