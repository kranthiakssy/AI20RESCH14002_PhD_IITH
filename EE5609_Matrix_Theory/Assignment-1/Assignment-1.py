# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 09:26:31 2020

@author: Kranthi Kumar P

EE5609 Matrix Theory

Assignment -1
"""
import numpy as np
import matplotlib.pyplot as plt

# angle of the straight line w.r.t to y-axis measured anticlockwise
ang = 30
print('Angle of the straight line w.r.t to y-axis measured anti clockwise = {0}'.format(ang))
# angle of the straight line w.r.t to x-axis measured anticlockwise
theta = 90 + ang

# Slope of line
slope = np.tan((np.pi/180)*theta)
print('Slope of the line = {0}'.format(slope))

