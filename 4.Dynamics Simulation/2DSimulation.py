

# -*- coding: utf-8 -*-
"""
Molecular Dynamics simulations of 2D simple liquid

"""
import numpy as np
import random
import matplotlib.pylab as pl
import matplotlib.animation as animation

Natom = 36
Nmax = 36
NT = 500
Tinit = 0.5
dens = 1.0
t1 = 0
x = np.zeros(Nmax)
y = np.zeros(Nmax)
vx = np.zeros(Nmax)
vy = np.zeros(Nmax)
fx = np.zeros([Nmax,2])
fy = np.zeros([Nmax,2])
L = int(1.0*Natom**0.5)
tt = np.arange(NT)
xc = np.zeros([Natom,NT])
yc = np.zeros([Natom,NT])


# Gaussian random number
def twelverans():
    s = 0.0
    for i in range(1,13):
        s = s + random.random()
    return s/12.0 - 0.5

def initialposvel():
    i = -1
    for ix in range(L):
        for iy in range(L):
            i = i + 1
            x[i] = ix
            y[i] = iy
            vx[i] = twelverans()
            vy[i] = twelverans()
            vx[i] = vx[i] * np.sqrt(Tinit)
            vy[i] = vy[i] * np.sqrt(Tinit)
def sign(a,b):
    if b>0:
        return abs(a)
    else:
        return -abs(a)

def forces(t, w, PE, PEorW):
    r2cut = 9
    PE = 0.0
    for i in range(0,Natom):
        fx[i][t] = 0.0
        fy[i][t] = 0.0
    for i in range(0,Natom-1):
        for j in range(i+1,Natom):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            if (dx > 0.5*L):
                dx = dx - L
            if (dx < -0.5*L):
                dx = dx + L

            if (dy > 0.5*L):
                dy = dy - L
            if (dy < -0.5*L):
                dy = dy + L

            r2 = dx*dx + dy*dy
            if(r2 < r2cut):
                invr2 = 1.0/r2
                invr6 = invr2**3
                wij = 48*invr2*invr6*(invr6-0.5)
                fijx = wij*dx
                fijy = wij*dy
                fx[i][t] = fx[i][t] + fijx
                fy[i][t] = fy[i][t] + fijy
                fx[j][t] = fx[j][t] - fijx
                fy[j][t] = fy[j][t] - fijy
                PE = PE + 4.0*(invr6)*(invr6-1)
                w = w + wij
    if(PEorW == 1):
        return PE
    else:
        return w

def timevolution():
    avKE = 0.0
    avPE = 0.0
    t1 = 0
    PE = 0.0
    h = 0.03
    hover2 = h/2.0
    # initialization KE & PE via forces
    KE = 0.0
    w = 0.0
    initialposvel()
    for i in range(0, Natom):
        KE = KE + (vx[i]*vx[i] + vy[i]*vy[i])/2
    PE = forces(t1, w, PE, 1)
    time = 1
    for it in np.arange (NT):
        if np.mod(it,100) == 0:
           print('it=',it)
        for i in range(0,Natom):
            PE = forces(t1, w, PE, 1)
            x[i] = x[i] + h*(vx[i] + hover2*fx[i][t1])
            y[i] = y[i] + h*(vy[i] + hover2*fy[i][t1])
            if x[i] <= 0:
               x[i]=x[i] + L
            if x[i] > L:
               x[i]=x[i] - L
            if y[i] <= 0:
               y[i]=y[i] + L
            if y[i] > L:
               y[i]=y[i] - L
            xc[i][it] = x[i]
            yc[i][it] = y[i]
        PE = 0.0
        t2 = 1
        PE = forces(t2, w, PE, 1)
        KE = 0.0
        w = 0.0

        for i in range(0, Natom):
            vx[i] = vx[i] + hover2*(fx[i][t1] + fx[i][t2])
            vy[i] = vy[i] + hover2*(fy[i][t1] + fy[i][t2])
            KE = KE + (vx[i]*vx[i] + vy[i]*vy[i])/2
    # averages
        avKE = avKE + KE
        avPE = avPE + PE
        time += 1
        t = time
        if(t == 0):
           t = 1
        eKavg = avKE/t
        ePavg = avPE/t
        #print(t,ePavg, eKavg, ePavg+eKavg)

timevolution()

def init():
    d.set_data([], [])
    return d,

def update_line(num, xc,yc,dot):
    dot.set_data(xc[:,num],yc[:,num])
    return dot,

fig1 = pl.figure()
#pl.plot(xx,yy)
d, = pl.plot([], [], 'ro',markersize=30)
pl.xlim(-0.5, 6.5)
pl.ylim(-0.5, 6.5)
pl.xlabel('X')
pl.ylabel('Y')
pl.title('MD')
dot_ani = animation.FuncAnimation(fig1, update_line, np.arange(500),\
fargs=(xc,yc,d),interval=20, init_func=init, blit=True)
#dot_ani.save('Brownian.mp4',fps=30)
pl.show()
