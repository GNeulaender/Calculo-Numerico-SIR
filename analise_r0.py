import csv
import numpy as np
import matplotlib.pyplot as plt
from constantes import omega, N

def smoother(C,n):
    Cs = C[2*n:]
    for i in range(-n+1,n+1):
        Cs += C[n-i:-(n+i)]
    return Cs/(2*n+1)

input_file = 'data/BR.csv'
C = np.genfromtxt(input_file, delimiter=',', usecols = (1))
Cs = smoother(C,2)
dC = Cs[1:] - Cs[:-1]
d2C = dC[1:] - dC[:-1]

Cs = Cs[2:]
dC = dC[1:]

alpha_max = 20
alpha_min = 10

mi = lambda alpha, C, dC: (alpha/(omega*N)) * (omega*C + dC)

r0 = lambda alpha, C, dC, d2C: (1/(1-mi(alpha,C,dC))) + (d2C/( omega*dC*(1-mi(alpha,C,dC)) ))

r0_max = r0(alpha_max, Cs, dC, d2C)
r0_min = r0(alpha_min, Cs, dC, d2C)
r0_aprox = (r0_max + r0_min)/2
