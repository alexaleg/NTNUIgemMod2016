import numpy as np
from scipy.optimize import minimize

""" Define parameters  """
R0 = 1

def dynamicsystem(X, t, U1, U2, KEQ):
    """ Setting up the system of ODEs:
        Input:
            X = Vector of compositions
            X[0]: D1
            X[1]: D2
            X[2]: R
            X[3]: RD1
            X[4]: RD2
            X[5]: RD1C
            X[6]: RD2C
            X[7]: RC
            X[8]: Phi
            X[9]: D12
            X[10]: U1
            X[11]: U2
            X[12]: U*
        Output:
           Array of derivatives in the same order.
        """


    """ Define reaction constants """
    # 1
    k1 = 9.0e-2
    # KD12 = 1400 Base case
    KD12 = 10**KEQ[0]

    q1 = k1 / KD12

    # 2-3
    k2 = 5.0e-3
    k3 = k2

    # KRD1 = 10 Base case
    KRD1 = 10**KEQ[1]
    KRD2 = KRD1
    q2 = k2 / KRD1
    q3 = k3 / KRD2

    # 4-5
    k4 = 0.534 / 60  # s-1
    k5 = k4

    # 6-7
    k6 = 1e3
    KRD1c = 10**KEQ[2]
    q6 = k6 / KRD1c
    k7 = k6
    q7 = q6

    # 8
    k8 = 1.5e-2  # s-1

    # 9 - 10
    k9 = 1.0e-2  # s-1
    k10 = k9

    # 11
    k11 = 3e-3  # s-1

    # 12
    k12 = 3.9e-4  # s-1

    # 13
    k13 = 3e-3  # s-1

    # 14
    k14 = 9.8e-2  # s-1

    # 15 - 16
    a1 = 1
    a2 = 1
    k16 = a1 * k14
    k15 = a2 * k14


    return np.array([-k1*X[0]*X[1]+q1*X[9]-k2*X[0]*X[2]+q2*X[3]-k9*X[0]+k15*U1 +k6*X[5]-q6*X[7]*X[0],
                     -k1*X[0]*X[1]+q1*X[9]-k3*X[1]*X[2]+q3*X[4]-k10*X[1]+k16*U2 +k7*X[6]-q7*X[7]*X[1] , # D2
                     -k2*X[0]*X[2]+q2*X[3]-k3*X[1]*X[2]+q3*X[4]-k13*X[2]+ k14*R0,
                      k2*X[0]*X[2]-q2*X[3]-k4*X[3]-k11*X[3],
                      k3*X[1]*X[2]-q3*X[4]-k5*X[4]-k11*X[4],
                      k4*X[3]-k6*X[5]+q6*X[7]*X[0]-k11*X[5],
                      k5*X[4]-k7*X[6]+q7*X[7]*X[1]-k11*X[6],
                      k6*X[5]-q6*X[7]*X[0]+k7*X[6]-q7*X[7]*X[1]-k11*X[7],
                      k8*X[7]-k12*X[8],
                      k1*X[0]*X[1]+q1*X[9]-k11*X[9]])



