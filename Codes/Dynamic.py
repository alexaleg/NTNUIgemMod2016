#!/Modelling/Dynamic.py
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from Data import dynamicsystem



# Integrate
Tmax = 100000
t = np.linspace(0, Tmax, 8*Tmax)              # time
X0 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

U1 = 1
U2 = 1
#Keq = [5,-1.5,3] # Ideal case
b = np.log10(1400)
Keq = [b,1,3]
X, infodict = integrate.odeint(dynamicsystem, X0, t, args=(U1,U2,Keq), full_output=True)
infodict['message']             # >>> 'Integration successful.'

#!python
plt.plot(t,X[:,0],'--',t, X[:,1],'--',t, X[:,2],t, X[:,3],t, X[:,4],t, X[:,5],t, X[:,6],t,X[:,7],t, X[:,8],t, X[:,9], '--')
legend = ["D1", "D1","R", "RD1","RD2","RD1C", "RD2C", "RC","Phi","D12"]
plt.legend(legend,loc='best')
plt.xlabel('Time [s]')
plt.ylabel('Molecules')
plt.savefig('./../Documentation/img/Dynamic.pdf')
plt.show()