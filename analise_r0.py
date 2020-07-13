import csv
import numpy as np
import matplotlib.pyplot as plt
from constantes import omega, N

input_file = 'data/BR.csv'
C = np.genfromtxt(input_file, delimiter=',', usecols = (1))
Cs = C
dC = Cs[1:] - Cs[:-1]
d2C = dC[1:] - dC[:-1]

alpha_max = 20
alpha_min = 10

mi = lambda alpha, dC, d2C: (alpha/(omega*N)) * (omega*C + dC)

r0 = lambda alpha, C, dC, d2C: (1/(1-mi(alpha,dC,d2C)) + (d2C/( omega*dC*(1-mi(alpha,dC,d2C)) ))
