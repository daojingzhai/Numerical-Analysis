# -*- coding: utf-8 -*-
"""
Shooting method solving wave equation.

"""
from numpy import arange, zeros, empty, math
import pylab as pl
import sys

# some parameters
L = 1.0
N = 100
dt = L/N
eps = 0.000001
k = 1.0
dk = 0.1
freturn = zeros(2)
psiphi = zeros(2)
psiphitemp = zeros(2)
XX = zeros(N)
PHIXX = zeros(N)
# Defining functions....
def f1(psiphi,k):
    freturn[0] = -k*k*psiphi[1]
    freturn[1] = psiphi[0]
    return freturn

def rk4(dt, k, N):#---四阶龙格库塔函数---
    psiphi[0] = 0.01
    psiphi[1] = 0.0
    t = 0

    for i in range(N):
        fR = f1(psiphi, k)
        k1 = fR[0]
        l1 = fR[1]

        psiphitemp[0] = psiphi[0] + k1*dt/2
        psiphitemp[1] = psiphi[1] + l1*dt/2
        fR = f1(psiphitemp, k)
        k2 = fR[0]
        l2 = fR[1]

        psiphitemp[0] = psiphi[0] + k2*dt/2
        psiphitemp[1] = psiphi[1] + l2*dt/2
        fR = f1(psiphitemp, k)
        k3 = fR[0]
        l3 = fR[1]

        psiphitemp[0] = psiphi[0] + k3*dt
        psiphitemp[1] = psiphi[1] + l3*dt
        fR = f1(psiphitemp, k)
        k4 = fR[0]
        l4 = fR[1]
#---------Runge Kutta-----
        psiphi[0] = psiphi[0] + (k1 + 2*k2 + 2*k3 +k4)*dt/6 #---Psi
        psiphi[1] = psiphi[1] + (l1 + 2*l2 + 2*l3 +l4)*dt/6 #---Phi

        XX[i] = t
        PHIXX[i] = psiphi[1]
        t = t + dt
    return psiphi

psiphi = rk4(dt, k, N)
phiold = psiphi[1]

while abs(dk) > eps:
    k = k + dk
    psiphi = rk4(dt,k,N)
    phinew = psiphi[1]
    if phinew*phiold > 0:
       continue
    k = k - dk
    dk = dk/2
print('k=',k)

pl.plot(XX, PHIXX, 'r-', label='phi',linewidth=1.0)
pl.legend(loc='upper right')
pl.show()
