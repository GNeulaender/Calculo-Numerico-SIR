import numpy as np

omega = 0.14 #Constante de taxa de remoção
r = lambda t: 1.5 #Aproximação para função r0(t)
dt = 1 #Constante de variação de tempo

#Definindo vetorialmente o modelo SIR
u = np.array([np.float32, np.float32, np.float32])

#Sistema de EDO em forma vetorial
f1 = lambda t,u: - omega * r(t) * (u[1]*u[0])/sum(u) # dS/st
f2 = lambda t,u: - omega * (r(t) * (u[1]*u[0])/sum(u) - u[1]) # dI/dt
f3 = lambda t,u: - omega * u[1] # dR/dt
f = lambda t,u: np.array([f1(t,u), f2(t,u), f3(t,u)]) # du/dt

#Declarações para Runge-Kutta de quarta ordem
k1 = lambda t, dt, u: dt * f(t,u)
k2 = lambda t, dt, u: dt * f(t + dt/2,u + k1/2)
k3 = lambda t, dt, u: dt * f(t + dt/2,u + k2/2)
k4 = lambda t, dt, u: dt * f(t + dt,u + k3)
k = lambda t, dt, u: (1/6)*(k1 + 2*k2 + 2*k3 + k4) #soma para aplicação