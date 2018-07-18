# -*- coding: utf-8 -*-
"""
2nd Runge-Kutta method solving RLC circuit ODE.

"""
from numpy import array, arange, zeros, empty, linalg, math
import pylab as pl
R = 1.0
L = 9.0
C = 8.0
V0 = 0.7
W = 0.25
dt = 0.01   
n = 50000
t = 0.0
Q = 1.0
I = 0.0

Qt=[]
It=[]
time = []
for k in range(n):
    t = t + dt
    V = V0*math.sin(W*t)
    Ihalf = I + (V - I*R - Q/C)/L*0.5*dt
    Qhalf = Q + I*0.5*dt
    I = I + dt*(V - Ihalf*R - Qhalf/C)
    Q = Q + Ihalf*dt
    Qt.append(Q)
    It.append(I)
    time.append(t)
pl.plot(time,Qt,'r-',label='2nd-RK-Q')
pl.plot(time,It,'k-',label='2nd-RK-I')
pl.xlabel('Time')
pl.ylabel('charge, I')
pl.xlim(0,500)
pl.ylim(-5.5,5.5)
pl.legend(loc='upper right')
pl.show()
