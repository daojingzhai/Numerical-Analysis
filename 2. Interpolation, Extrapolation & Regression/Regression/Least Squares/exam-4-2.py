# -*- coding: utf-8 -*-
"""
Created on Tue Jun 5 13:03:47 2018

@author: Daojing
"""

import numpy as np
from scipy import interpolate
import pylab as pl

xy = np.loadtxt("data.dat",float)
txy = np.transpose(xy)
covxy = np.cov(txy)

eigenValues,eigenVectors = np.linalg.eig(covxy)
idx = eigenValues.argsort()
eigenValues = eigenValues[1-idx]
eigenVectors = eigenVectors[:,1-idx]
print(eigenValues)
print(eigenVectors)
print(txy)
newxy = np.dot(eigenVectors,txy)
newtxy = np.transpose(newxy)
print(newtxy)


fig = pl.figure(figsize=(10,4))
ax1 =fig.add_subplot(1,2,1)
ax2 =fig.add_subplot(1,2,2)
ax1.plot(xy[:,0], xy[:,1], 'ks')
ax1.set_xlim(0,3.5)
ax1.set_ylim(0,3.5)

ax1.set_xlabel("X")
ax1.set_ylabel("Y")

ax2.plot(newtxy[:,0], newtxy[:,1], 'ks')
ax2.set_xlim(-4.0,-0.5)
ax2.set_ylim(-1.75,1.75)
ax2.set_xlabel("Xnew")
ax2.set_ylabel("Ynew")

pl.show()
