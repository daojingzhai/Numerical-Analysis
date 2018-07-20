# -*- coding: utf-8 -*-
"""
    Drunk Man Random Walk - Monte Carlo Method - Square Distance
    
"""
import numpy as np
import matplotlib.pylab as pl
import random
pi = 3.1415937
nwalk = 10000
nstep = 100
x = np.zeros(nwalk)
y = np.zeros(nwalk)
r2 = np.zeros(nwalk)
sum_walk = np.zeros(nstep)

for iwalk in range(nwalk):
    random.seed(None)
    x[iwalk] = 0
    y[iwalk] = 0
    r2[iwalk] = 0
    for istep in range(nstep):
        dx = 2*random.random()-1
        dy = 2*random.random()-1
        dr = np.sqrt(dx**2+dy**2)
        x[iwalk] = x[iwalk] + dx/dr
        y[iwalk] = y[iwalk] + dy/dr
        r2[iwalk] = x[iwalk]**2 + y[iwalk]**2
        sum_walk[istep] = sum_walk[istep] + r2[iwalk]
for istep in range(nstep):
    sum_walk[istep] = sum_walk[istep]/nwalk

time = np.arange(nstep)
pl.plot(time, sum_walk, 'r-', label='distribution',linewidth=1.0)
pl.xlim(0,100)
pl.ylim(0,120)
pl.xlabel(r'walk steps', fontsize=20)
pl.ylabel(r'<r2>', fontsize=20)
pl.show()
