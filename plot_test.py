import numpy as np
import matplotlib.pyplot as plt
from runge_kutta import runge_kutta

#Declaração de dados iniciais
u = np.array([10000,10,0]) #Condição inicial do sistema SIR
t0 = 0 #Tempo inicial
dt = 1 #Tamanho do passo

#Variáveis para o plot no gráfico
S = np.array([]) 
I = np.array([]) 
R = np.array([]) 
x = np.array([]) 

for t in range(t0,t0 + 365,dt):
    u = runge_kutta(t0 + t, dt, u)
    S = np.append(S, u[0])
    I = np.append(I, u[1])
    R = np.append(R, u[2])
    x = np.append(x, t0 + t)
    if u[1] <= 1: break

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, S, label='S')  # Plot some data on the axes.
ax.plot(x, I, label='I')  # Plot more data on the axes...
ax.plot(x, R, label='R')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.savefig('grafico.svg')
