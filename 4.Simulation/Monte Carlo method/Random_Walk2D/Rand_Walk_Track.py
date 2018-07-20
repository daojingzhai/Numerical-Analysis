# -*- coding: utf-8 -*-
"""
Drunk men Random Walk - Monte-Carlo Simulation - Track
"""
import numpy as np
import matplotlib.pylab as pl
import random

nmax = 10000
random.seed(None)
xx = []
yy = []

x = 0
y = 0
xx.append(x)
yy.append(y)

fig = pl.figure()
ax1 =fig.add_subplot(1,1,1)
walk = None
for i in range(nmax):
    oldcol = walk
    dx = 2*random.random()-1
    dy = 2*random.random()-1
    dr = np.sqrt(dx**2+dy**2)
    x = x + dx/dr
    y = y + dy/dr
    xx.append(x)
    yy.append(y)

walk = ax1.plot(xx, yy, 'r-',linewidth=1.0)
ax1.set_xlim(-50,50)
ax1.set_ylim(-50,50)
ax1.set_xlabel(r'X', fontsize=20)
ax1.set_ylabel(r'Y', fontsize=20)
pl.show()
