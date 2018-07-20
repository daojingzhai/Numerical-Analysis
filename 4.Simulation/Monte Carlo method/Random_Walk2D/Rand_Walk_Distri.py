# -*- coding: utf-8 -*-
"""
Drunk Man Random Walk - Monte Carlo Method - Gaussian distribution

"""
import numpy as np
import matplotlib.pylab as pl
import random
pi = 3.1415937
nwalk = 10000
nstep = 100
xr = np.zeros(nwalk)
yr = np.zeros(nwalk)
for iwalk in range(nwalk):
    random.seed(None)
    x = 0
    y = 0
    for istep in range(nstep):
        dx = 2*random.random()-1
        dy = 2*random.random()-1
        dr = np.sqrt(dx**2+dy**2)
        x = x + dx/dr
        y = y + dy/dr
        xr[iwalk] = x
        yr[iwalk] = y

xhist, xedge = np.histogram(xr,bins = 20)
xhist = xhist/len(xr)
yhist, yedge = np.histogram(yr,bins = 20)
yhist = yhist/len(yr)

xx = 0.5*(xedge[0:-1]+xedge[1:])
yy = 0.5*(yedge[0:-1]+yedge[1:])

fig = pl.figure(figsize=(10,4))
ax1 =fig.add_subplot(1,2,1)
ax2 =fig.add_subplot(1,2,2)
ax1.plot(xx, xhist, 'r-', label='distribution',linewidth=1.0)
ax2.plot(yy, yhist, 'b-', label='distribution',linewidth=1.0)
ax1.set_xlabel(r'X', fontsize=20)
ax1.set_ylabel(r'distribution', fontsize=20)
ax2.set_xlabel(r'Y', fontsize=20)
ax2.set_ylabel(r'distribution', fontsize=20)
ax1.set_xlim(-30,30)
ax1.set_ylim(0,0.2)
ax2.set_xlim(-30,30)
ax2.set_ylim(0,0.2)
pl.show()
