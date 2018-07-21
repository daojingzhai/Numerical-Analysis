# -*- coding: utf-8 -*-
"""
1D Heat Diffusion - Infinite Difference Method

"""
from numpy import arange, zeros, empty, math
import pylab as pl
import sys

A = 1/60.
H = 0.05
NT = 10000
U = zeros([21,NT+1])
Time = arange(0,NT,1)
XXX = arange(0,21*H,H)


for k in range(NT):
    U[0,k] = 0.0
    U[20,k] = 0.0

for i in range(1,20):
    U[i,0]=4*i*H*(1-i*H)

for k in range(NT):
    for i in range(1,20):
        U[i,k+1]=A*U[i+1,k]+(1-2*A)*U[i,k]+A*U[i-1,k]


fig = pl.figure(figsize=(10,4))
ax1 =fig.add_subplot(1,2,1)
ax2 =fig.add_subplot(1,2,2)

ax1.plot(XXX,U[:,0], 'r-', label='NT=0',linewidth=1.0)
ax1.plot(XXX,U[:,3000], 'b-', label='NT=3000',linewidth=1.0)
ax1.plot(XXX,U[:,6000], 'k-', label='NT=6000',linewidth=1.0)
ax1.set_ylabel(r'U', fontsize=20)
ax1.set_xlabel(r'X', fontsize=20)
ax1.set_xlim(0,1)
ax1.set_ylim(-0.2,1.2)
ax1.legend(loc='upper right')

extent = [0,NT+1,0,1]
levels = arange(0.0,1.0,0.01)
cs = ax2.contourf(U,levels,origin='lower',extent=extent,cmap=pl.cm.hot)
ax2.set_ylabel(r'X', fontsize=20)
ax2.set_xlabel(r'Time', fontsize=20)
pl.show()
