# -*- coding: utf-8 -*-
"""
Diffusion limited aggregation via Monte Carlo Method
    
"""
import numpy as np
import matplotlib.pylab as pl
import random

nrun = 1000000
xx = np.zeros(nrun)
yy = np.zeros(nrun)

xx[0] = 0.5
yy[0] = 0.0

for irun in range(1,nrun):
    if np.mod(irun,10000) == 0:
        print(irun)

    rand = random.random()
    if rand < 0.1:
       xx[irun] = 0.05*xx[irun-1]
       yy[irun] = 0.6*yy[irun-1]
    elif rand >= 0.1 and rand < 0.2:
       xx[irun] = 0.05*xx[irun-1]
       yy[irun] = -0.5*yy[irun-1] + 1.0
    elif rand >= 0.2 and rand < 0.4:
         xx[irun] = 0.46*xx[irun-1]-0.32*yy[irun-1]
         yy[irun] = 0.39*xx[irun-1]+0.38*yy[irun-1] + 0.6
    elif rand >= 0.4 and rand < 0.6:
         xx[irun] = 0.47*xx[irun-1]-0.15*yy[irun-1]
         yy[irun] = 0.17*xx[irun-1]+0.42*yy[irun-1] + 1.1
    elif rand >= 0.6 and rand < 0.8:
         xx[irun] = 0.43*xx[irun-1]+0.28*yy[irun-1]
         yy[irun] = -0.25*xx[irun-1]+0.45*yy[irun-1] + 1.0
    else:

        xx[irun] = 0.42*xx[irun-1]+0.26*yy[irun-1]
        yy[irun] = -0.35*xx[irun-1]+0.31*yy[irun-1] +0.7

pl.plot(xx, yy, 's', markersize=1)
pl.xlim(-1.5,1.5)
pl.ylim(-0.5,2.5)
pl.xlabel(r'X', fontsize=20)
pl.ylabel(r'Y', fontsize=20)
pl.show()
