import numpy as np
import matplotlib.pyplot as plt
from runge_kutta import runge_kutta
from habitantes_federacao import N

#Declaração de dados iniciais
u = np.array([N['MG']-7,7,0]) #Condição inicial do sistema SIR
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
    #if u[1] <= 1: break

fig, ax1 = plt.subplots()  # Cria a figura e o axis para S e R

color = 'tab:blue'
ax1.set_xlabel('tempo (dias)') # Configura o nome do axis x
ax1.set_ylabel('não-infectados') # Configura o nome do axis y para S e R
ax1.plot(x, S, label='S', color=color)  # Plota S como linha simples
ax1.plot(x, R, '--', label='R', color=color)  # Plota R como linha pontilhada
ax1.tick_params(axis='y', labelcolor=color) # Configura a cor e escala do axis y para I

ax2 = ax1.twinx() # Cria um novo axis para I

color = 'tab:red' # Cor para I
ax2.set_ylabel('infectados') #Configura o nome do axis y para I
ax2.plot(x, I, label='I', color=color)  # Plota I como linha simples
ax2.tick_params(axis='y', labelcolor=color) # Configura a cor e escala do axis y para I

ax1.set_title("Teste de Simulação")  # Adiciona um título ao gráfico
ax1.legend()  # Adiciona legenda para os plots em ax1
#ax2.legend()  # Adiciona legenda para os plots em ax2

plt.show() # Mostra o plot em uma janela externa
#plt.savefig('grafico.svg') # Salva o arquivo do plot como .svg

plt.close()
