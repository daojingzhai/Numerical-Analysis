# -*- coding: utf-8 -*-
"""
Monte Carlo integral to Find Pi 

"""
import numpy as np
import pylab as pl
import random
import sys
nmax = 100000
r0 = 1.0
seed = 135971
xr = np.zeros(nmax)
yr = np.zeros(nmax)
r2 = np.zeros(nmax)
random.seed(seed)
m = 0

for i in range(nmax):
    xr[i] = (2*random.random()-1)*r0
    yr[i] = (2*random.random()-1)*r0
    r2[i] = xr[i]**2 + yr[i]**2

    if(r2[i] < r0**2):
       m = m + 1
pi = 4.0*m/nmax
print('pi=',pi)

pl.plot(xr,yr, 'r.', label='scattering')
pl.xlim(-1,1)
pl.ylim(-1,1)
pl.xlabel(r'random number', fontsize=20)
pl.ylabel(r'distribution', fontsize=20)
pl.show()
