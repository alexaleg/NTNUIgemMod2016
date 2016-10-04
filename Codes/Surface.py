#!/Modelling/Dynamic.py
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from Data import dynamicsystem
from matplotlib.mlab import griddata



# Integrate

Umin = 0.02
Umax = 1

def surface(EQ):

    Np = 10
    u1 = np.linspace(Umin, Umax, Np)
    u2 = u1
    Tmax = 100000
    t = np.linspace(0, Tmax, 8 * Tmax)  # time
    X0 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    phi = np.zeros(Np ** 2)
    x = np.zeros(Np ** 2)
    y = np.zeros(Np ** 2)
    n = 0
    for i in u1:
        for j in u2:
            X, infodict = integrate.odeint(dynamicsystem, X0, t, args=(i,j,EQ), full_output=True)

            phi[n] = X[-1,8]
            x[n] = i
            y[n] = j
            print n
            n += 1

    Np2 = 200
    u1 = np.linspace(Umin, Umax, Np2)
    u2 = u1
    #print x.size(),y.size(), phi.size()

    Phi = griddata(x, y, phi, u1, u2, interp='linear')
    return Phi, u1, u2

def plotresults(Phi, U1, U2, EQ, n):
    Nl = 100

    fig = plt.figure(n)
    plt.title(str(EQ))
    plt.contourf(U1/Umax,U2/Umax,Phi,Nl,cmap=plt.cm.RdBu)
    cbar = plt.colorbar()
    cbar.set_label('Pigment Molecules')
    plt.xlabel('U1/Umax')
    plt.ylabel('U2/Umax')
    return fig

b = np.log10(1400) # For base case
EQlist = [ [b,1,3], [5,-1.5,3]] # Base case and optimal
nr = 1

for EQ in EQlist:
    Z, Y, X = surface(EQ)
    plotresults(Z,Y,X,EQ,nr)
    name = './../Documentation/img/Surface%s.pdf'%nr
    plt.savefig(name)
    nr +=1

plt.show()



#!python
