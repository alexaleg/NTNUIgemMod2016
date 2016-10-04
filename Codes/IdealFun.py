import numpy as np
import matplotlib.pyplot as plt

min = 0
max = 1

Np = 50
X = np.linspace(min,max,Np)
Y = X
a = 10
b = 1
X, Y = np.meshgrid(X, Y)
Z = a*(X**2 +Y**2-2*X*Y*b)

def plotresults(Phi, U1, U2, n):
    Nl = 100
    fig = plt.figure(n)
    plt.title('Ideal function')
    plt.contourf(U1,U2,Phi,Nl,cmap=plt.cm.RdBu)
    cbar = plt.colorbar()
    cbar.set_label('A XOR B')
    plt.xlabel('A')
    plt.ylabel('B')
    return fig

plotresults(Z, X, Y, 1)
plt.savefig('./../Documentation/img/IdealSurface.pdf')
plt.show()
