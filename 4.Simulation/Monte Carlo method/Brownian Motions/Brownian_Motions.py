# -*- coding: utf-8 -*-
"""
    Solve Langevin Equation: Simulating Brownian motions by Monte Carlo Method

"""
import numpy as np
import matplotlib.pylab as pl
import matplotlib.animation as animation
import random

nx = 1000
nt = 1000000
dx = 0.1
dt = 0.001
x0 = -5
ksai = 0.1
Temp = 0.9
K=1.0
xx = np.zeros(nx)
time = np.zeros(nt)

u = np.zeros(nx)
for i in range(nx):
    xx[i] = x0 + i*dx
for it in range(nt):
    time[it] = it*dt
for i in range(nx):
    x = x0 + i*dx
    u[i] = K*(x-1)**2*(x+2)**2


xt = np.zeros(nt)
energy = np.zeros(nt)
energy[0] = K*(xt[0]-1)**2*(xt[0]+2)**2

for it in range(nt-1):
    fx = -2.0*K*(xt[it]-1.0)*(xt[it]+2.0)*(2.0*xt[it]+1.0)
    xt[it+1] = xt[it] + 1.0/ksai*fx*dt
    rnormal = random.gauss(0,1)
    fB = np.sqrt(2*Temp/ksai/dt)*rnormal
    xt[it+1] = xt[it+1] + fB*dt
    v = (xt[it+1]-xt[it])/dt
    energy[it+1] = K*(xt[it+1]-1)**2*(xt[it+1]+2)**2

hist, xedge = np.histogram(xt,bins = 20)
hist = hist/len(xt)
print(hist)
x = 0.5*(xedge[0:-1]+xedge[1:])

fig = pl.figure(figsize=(10,4))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.plot(time, xt, 'r.', linewidth=1.0)
ax2.plot(x,hist,'r-', linewidth=1.0)
ax1.set_xlabel(r'Time', fontsize=20)
ax1.set_ylabel(r'Position', fontsize=20)
ax2.set_xlabel(r'Position', fontsize=20)
ax2.set_ylabel(r'Distribution', fontsize=20)
pl.show()
