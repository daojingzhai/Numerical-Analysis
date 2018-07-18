# -*- coding: utf-8 -*-
"""
Euler-Modify method solving RC circuit ODE. 

"""
from numpy import array, arange, zeros, empty, linalg, math
import pylab as pl
rc = 2.0
dt = 0.5
n = 1000
t = 0.0
q = 1.0
qt=[]
qt0=[]
time = []
for i in range(n):
    t = t + dt
    q1 = q - q*dt/rc
    q = q - 0.5*(q1*dt/rc + q*dt/rc)
    q0 = math.exp(-t/rc)
    qt.append(q)
    qt0.append(q0)
    time.append(t)

pl.plot(time,qt,'ro',label='Euler-Modify')
pl.plot(time,qt0,'k-',label='Analytical')
pl.xlabel('Time')
pl.ylabel('charge')
pl.xlim(0,12)
pl.ylim(-0.2,1.0)
pl.legend(loc='upper right')
pl.show()
