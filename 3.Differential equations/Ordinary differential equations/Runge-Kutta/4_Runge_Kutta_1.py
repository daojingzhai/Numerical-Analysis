# -*- coding: utf-8 -*-
"""
4th Runge-Kutta method solving Damped Pendulum equation

"""
from numpy import arange, empty, math
import pylab as pl
import sys
t = 0.0
g=9.8
xl=1.
q = 1.0
dt=0.04
theta=0.2
omiga=0.
n = 2000

ThetaT0 = []
OmigaT0 = []
Time0 = []
for i in range(n):
    xk1=-(g/xl)*theta-q*omiga
    xl1=omiga
    xk2=-(g/xl)*(theta+dt/2.*xl1)-q*(omiga+dt/2.*xk1)
    xl2=omiga+dt/2.*xk1
    xk3=-(g/xl)*(theta+dt/2.*xl2)-q*(omiga+dt/2.*xk2)
    xl3=omiga+dt/2.*xk2
    xk4=-(g/xl)*(theta+dt*xl3)-q*(omiga+dt*xk3)
    xl4=omiga+dt*xk3

    omiga=omiga+dt/6.*(xk1+2*xk2+2*xk3+xk4)
    theta=theta+dt/6.*(xl1+2*xl2+2*xl3+xl4)
    t=t+dt
    ThetaT0.append(theta)
    OmigaT0.append(omiga)
    Time0.append(t)

fig = pl.figure(figsize=(10,4))
ax1 =fig.add_subplot(1,2,1)
ax2 =fig.add_subplot(1,2,2)

ax1.plot(Time0, ThetaT0, 'r-', label='q=1.0',linewidth=2.0)
ax2.plot(ThetaT0, OmigaT0, 'r-', label='q=1.0',linewidth=2.0)

ax1.set_ylabel(r'Theta', fontsize=20)
ax1.set_xlabel(r'Time', fontsize=20)
ax1.set_xlim(0,10)
ax1.set_ylim(-0.3,0.3)
ax2.set_ylabel(r'Theta', fontsize=20)
ax2.set_xlabel(r'OmigaT', fontsize=20)
ax2.set_xlim(-0.3,0.3)
ax2.set_ylim(-0.6,0.6)
pl.legend(loc='upper right')
#pl.show()

#sys.exit(0)
#---------------------------
# q = 5.0
t = 0.0
g=9.8
xl=1.
q = 5.0
dt=0.04
theta=0.2
omiga=0.
n = 2000

ThetaT1 = []
OmigaT1 = []
Time1 = []
for i in range(n):
    xk1=-(g/xl)*theta-q*omiga
    xl1=omiga
    xk2=-(g/xl)*(theta+dt/2.*xl1)-q*(omiga+dt/2.*xk1)
    xl2=omiga+dt/2.*xk1
    xk3=-(g/xl)*(theta+dt/2.*xl2)-q*(omiga+dt/2.*xk2)
    xl3=omiga+dt/2.*xk2
    xk4=-(g/xl)*(theta+dt*xl3)-q*(omiga+dt*xk3)
    xl4=omiga+dt*xk3

    omiga=omiga+dt/6.*(xk1+2*xk2+2*xk3+xk4)
    theta=theta+dt/6.*(xl1+2*xl2+2*xl3+xl4)
    t=t+dt
    ThetaT1.append(theta)
    OmigaT1.append(omiga)
    Time1.append(t)

ax1.plot(Time1, ThetaT1, 'k-', label='q=5.0',linewidth=2.0)
ax2.plot(ThetaT1, OmigaT1, 'k-', label='q=5.0',linewidth=2.0)

#---------------------------
# q = 10.0
t = 0.0
g=9.8
xl=1.
q = 10.0
dt=0.04
theta=0.2
omiga=0.
n = 2000

ThetaT2 = []
OmigaT2 = []
Time2 = []
for i in range(n):
    xk1=-(g/xl)*theta-q*omiga
    xl1=omiga
    xk2=-(g/xl)*(theta+dt/2.*xl1)-q*(omiga+dt/2.*xk1)
    xl2=omiga+dt/2.*xk1
    xk3=-(g/xl)*(theta+dt/2.*xl2)-q*(omiga+dt/2.*xk2)
    xl3=omiga+dt/2.*xk2
    xk4=-(g/xl)*(theta+dt*xl3)-q*(omiga+dt*xk3)
    xl4=omiga+dt*xk3

    omiga=omiga+dt/6.*(xk1+2*xk2+2*xk3+xk4)
    theta=theta+dt/6.*(xl1+2*xl2+2*xl3+xl4)
    t=t+dt
    ThetaT2.append(theta)
    OmigaT2.append(omiga)
    Time2.append(t)

ax1.plot(Time2, ThetaT2, 'b-', label='q=10.0',linewidth=2.0)
ax2.plot(ThetaT2, OmigaT2, 'b-', label='q=10.0',linewidth=2.0)

pl.legend(loc='upper right')
pl.show()
