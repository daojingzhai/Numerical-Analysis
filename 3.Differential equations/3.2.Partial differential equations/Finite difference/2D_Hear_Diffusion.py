# -*- coding: utf-8 -*-
"""
2D Heat Diffusion - Infinite Difference Method

"""
from numpy import arange, zeros, empty, math
import pylab as pl
import sys

N = 50
M = 50
M1 = 20
M2 = 30
D = 2
H = 1.0
DT = 0.1
MT = 10000
NX = N+1
MX = M+1
S=DT*D/H**2
if S > 0.25:
   print('S should be less than 0.25')
   exit()
C1 = zeros([NX+1,MX+1])
C2 = zeros([NX+1,MX+1])

for i in range(NX):
    for j in range(MX):
        C1[i,j] = 0.0

for j in range(M1,M2+1,1):
    C1[0,j] = 1.0

for k in range(MT):
    for i in range(1,N):
        for j in range(1,M):
            C2[i,j] = (1-4.0*S)*C1[i,j]+ \
            S*(C1[i+1,j]+C1[i-1,j]+C1[i,j+1]+C1[i,j-1])
    for j in range(1,M):
        for i in range(1,N):
            C1[i,j] = C2[i,j]
        C1[N,j] = C2[N-1,j]

    for i in range(1,M1+1):
        C1[0,i] = C2[1,i]
    for i in range(M2,MX):
        C1[0,i] = C2[1,i]

fig = pl.figure(figsize=(5,4))
ax1 =fig.add_subplot(1,1,1)
extent = [0,N,0,M]
levels = arange(0.0,1.0,0.01)
#ax1.contourf(C1,levels,origin='lower',extent=extent,cmap=pl.cm.jet)
ax1.contourf(C1,levels,origin='lower',extent=extent,cmap=pl.cm.RdBu)
ax1.set_ylabel(r'X', fontsize=20)
ax1.set_xlabel(r'Y', fontsize=20)
pl.show()
