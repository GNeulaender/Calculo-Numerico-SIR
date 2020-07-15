import numpy as np
from constantes import gamma #Constante de taxa de remoção

#r = lambda t: 2.6 #Aproximação para função r0(t)
#r = lambda t: 1.282 + 3.5658*np.exp(-t/7.80892) #Aproximação para função r0(t)
dt = 1 #Constante de variação de tempo

#Condições iniciais pro sistema
u = np.array([np.float32, np.float32, np.float32]) #Entradas de u = (S, I, R)

#Sistema de EDO em forma vetorial
f1 = lambda t,u,r: - gamma * r(t) * (u[1]*u[0])/sum(u) # dS/st
f2 = lambda t,u,r: gamma * (r(t) * ((u[1]*u[0])/sum(u)) - u[1]) # dI/dt
f3 = lambda t,u,r: gamma * u[1] # dR/dt
f = lambda t,u,r: np.array([f1(t,u,r), f2(t,u,r), f3(t,u,r)]) # du/dt

#Declarações para Runge-Kutta de quarta ordem
k1 = lambda t, dt, u, r: dt * f(t,u,r)
k2 = lambda t, dt, u, r: dt * f(t + dt/2,u + k1(t,dt,u,r)/2,r)
k3 = lambda t, dt, u, r: dt * f(t + dt/2,u + k2(t,dt,u,r)/2,r)
k4 = lambda t, dt, u, r: dt * f(t + dt,u + k3(t,dt,u,r),r)
k = lambda t, dt, u, r: (1/6)*(k1(t,dt,u,r) + 2*k2(t,dt,u,r) + 2*k3(t,dt,u,r) + k4(t,dt,u,r)) #soma para aplicação

#Runge-Kutta completo
def runge_kutta(t,dt,u,r):
    return u + k(t,dt,u,r)
