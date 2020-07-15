import numpy as np
import matplotlib.pyplot as plt
from runge_kutta import runge_kutta
from constantes import state, N, r0_fixo, r0_funcao

#Declaração de dados iniciais
u = np.array([N[state]-7,7,0]) #Condição inicial do sistema SIR
t0 = 0 #Tempo inicial
dt = 1 #Tamanho do passo

def plot_simulation(state,title,export_file,t0,tf,dt,u,r0):
    #Variáveis para o plot no gráfico
    S = np.array([]) 
    I = np.array([]) 
    R = np.array([]) 
    x = np.array([]) 
    
    # Simulação usando o método de Runge Kutta
    for t in range(t0,t0 + tf,dt):
        u = runge_kutta(t0 + t, dt, u, r0)
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
    
    ax1.set_title(title)  # Adiciona um título ao gráfico
    #ax1.set_title(title + ' - ' + state)  # Adiciona um título ao gráfico
    ax1.legend()  # Adiciona legenda para os plots em ax1
    #ax2.legend()  # Adiciona legenda para os plots em ax2
    
    #plt.show() # Mostra o plot em uma janela externa
    export_file = 'simulacoes/' + export_file + '.svg' 
    plt.savefig(export_file) # Salva o arquivo do plot como .svg
    
    plt.close()

plot_simulation(state,"Simulação A: r0 fixo", 'SimulacaoA_r0fixo', t0, 140, dt, u, r0_fixo)
plot_simulation(state,"Simulação B: r0 variável", 'SimulacaoB_r0variavel', t0, 500, dt, u, r0_funcao)
