# -*- coding: utf-8 -*-
"""
1D Wave Function - Infinite Difference Method
    
"""
from numpy import arange, zeros, empty, math
import pylab as pl
import sys

PI=3.1415927
A=1
H=0.02
V=1
T=0.2
U = zeros([51,251])
Time = arange(0,250,1)
XXX = arange(0,51*H,H)

for i in range(51):
    U[i,0]=math.sin(i*PI*H)
    U[i,1]=math.sin(i*PI*H)+i*H*T*(1-i*H)

for j in range(250):
    U[0,j]=0
    U[50,j]=0

for j in range(1,250):
    for i in range(1,50):
        U[i,j+1]=U[i+1,j]+U[i-1,j]-U[i,j-1]

fig = pl.figure(figsize=(10,4))
ax1 =fig.add_subplot(1,2,1)
ax2 =fig.add_subplot(1,2,2)

ax1.plot(XXX,U[:,0], 'r-', label='NT=0',linewidth=1.0)
ax1.plot(XXX,U[:,15], 'b-', label='NT=15',linewidth=1.0)
ax1.plot(XXX,U[:,50], 'c-', label='NT=50',linewidth=1.0)
ax1.plot(XXX,U[:,80], 'k-', label='NT=80',linewidth=1.0)
ax1.set_ylabel(r'U', fontsize=20)
ax1.set_xlabel(r'X', fontsize=20)
ax1.set_xlim(0,1)
ax1.set_ylim(-2,2)
ax1.legend(loc='upper right')

extent = [0,250,0,50]
levels = arange(-2.0,2.0,0.01)
cs = ax2.contourf(U,levels,origin='lower',extent=extent,cmap=pl.cm.hot)
ax2.set_ylabel(r'X', fontsize=20)
ax2.set_xlabel(r'Time', fontsize=20)
pl.show()
