#Code by GVV Sharma
#July 15, 2020
#released under GNU GPL
#Drawing a ellipse

import numpy as np
import matplotlib.pyplot as plt

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

#Standard ellipse
a = 3
b = 4
x = ellipse_gen(a,b)

#Vertices
A1 = np.array([a,0])
A2 = -A1
B1 = np.array([0,b])
B2 = -B1

#Inputs
A = np.array([2,4])
B = np.array([3,2]) 
C = np.array([2,-4]) 
D = np.array([-3,2])  
m = np.array([1,0]) 
n = np.array([0,1]) 
k1=-4
k2=0
#Generating all lines
x_ax1 = line_dir_pt(m,A,k1,k2)
x_ay1 = line_dir_pt(n,B,k1,k2)
x_ax2 = line_dir_pt(m,C,k1,k2)
x_ay2 = line_dir_pt(n,D,k1,k2)

#Plotting all lines
plt.plot(x_ax1[0,:],x_ax1[1,:]) #,label='$\\parallel x$')
plt.plot(x_ay1[0,:],x_ay1[1,:]) #,label='$\\parallel y$')
plt.plot(x_ax2[0,:],x_ax2[1,:]) #,label='$\\parallel x$')
plt.plot(x_ay2[0,:],x_ay2[1,:]) #,label='$\\parallel y$')

#Plotting the ellipse
plt.plot(x[0,:],x[1,:],label='Ellipse')

#Labeling the coordinates
ellipse_coords = np.vstack((A1,A2,B1,B2)).T
plt.scatter(ellipse_coords[0,:], ellipse_coords[1,:])
vert_labels = ['$q_{1y}$','$q_{2y}$','$q_{1x}$', '$q_{2x}$']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (ellipse_coords[0,i], ellipse_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('./figs/ellipse.pdf')
plt.savefig('./ellipse.eps')
plt.savefig('./ellipse.png')
#subprocess.run(shlex.split("termux-open ./figs/ellipse.pdf"))
#else
#plt.show()
#
#
#
#
#
#
#
