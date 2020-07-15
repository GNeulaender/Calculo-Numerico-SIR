import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from constantes import gamma
from habitantes_federacao import N

#Valores das constantes 'alpha'
alpha_max = 20
alpha_min = 10

#Declaração de mi(t)
mi = lambda alpha, N, C, dC_s: (alpha/(gamma*N)) * (gamma*C + dC_s)
#Declaração de r0(t)
r0 = lambda alpha, N, C, dC_s, d2C_s: (1/(1-mi(alpha,N,C,dC_s))) + (d2C_s/(gamma*dC_s*(1-mi(alpha,N,C,dC_s)) ))

#Função de suavisação dos dados de casos novos
def smoother(C, n):
    left_ext = np.full((n,),C[0])
    k = len(C) - 1 #Ultimo elemento de C
    right_ext = np.fromfunction(lambda j: C[k] + C[k-n+(j+1)] - C[k-n], (n,), dtype=int)

    C = np.append(left_ext, C)
    C = np.append(C, right_ext)

    C_s = np.array(C[2*n:]) #Primeira soma (caso 'i=-n')
    for i in range(-n+1,n+1): #Somatoria de 'i=-n+1' a 'n'
        C_s += C[n-i:-(n+i)]
    return C_s/(2*n+1) #Média simples dos '2n+1' termos

#Importa dados do estado 'state' com suavisação 'n'
def import_data(state, n, cycles):
    input_file = 'data/' + state + '.csv' #Nome do arquivo de entrada
    C = np.genfromtxt(input_file, delimiter=',', usecols = (1)) #Importa dados dos casos acumulados
    #Calcula derivadas NÃO suavisadas
    dC = np.array(C[1:] - C[:-1]) #Primeira derivada (casos novos)
    d2C = np.array(dC[1:] - dC[:-1]) #Segunda derivada

    #Suavisa dado dos casos acumulados
    C_s = np.array(C)
    for i in range(0,cycles):
        C_s = smoother(C_s,n)

    #Calcula derivadas suavisadas
    dC_s = np.array(C_s[1:] - C_s[:-1]) #Primeira derivada (casos novos)
    d2C_s = np.array(dC_s[1:] - dC_s[:-1]) #Segunda derivada
    
    #Concatena arrays para terem a mesma dimensão
    #NÃO Suavisadas
    C = C[2:]
    dC = dC[1:]
    #Suavisadas
    C_s = C_s[2:]
    dC_s = dC_s[1:]

    return C, dC, C_s, dC_s, d2C_s #Retorna dados formatados

def generate_data(N, C_s, dC_s, d2C_s): #Gera r0
    r0_max = r0(alpha_max, N, C_s, dC_s, d2C_s) #Calcula r0 máximo
    r0_min = r0(alpha_min, N, C_s, dC_s, d2C_s) #Calcula r0 mínimo
    r0_aprox = (r0_max + r0_min)/2 #Calcula melhor aproximação (média simples)

    return r0_max, r0_min, r0_aprox

def plot_graphs(state, data, data_s, data_r0):
    #Cria entradas para eixo 'x'
    x = np.arange( len(data[0]) ) 
    x_s = np.arange( len(data_s[0]) ) 
    x_r0 = np.arange( len(data_r0[0]) ) 

    #Cria figura de pyplot e configura o layout
    fig = plt.figure(constrained_layout=True)
    gs = gridspec.GridSpec(ncols=2, nrows=2, figure=fig)

    #Plota dados da figura 0
    f_ax0 = fig.add_subplot(gs[0,0])
    f_ax0.set_title('Casos acumulados - ' + state)
    f_ax0.set_ylabel('Casos')
    f_ax0.set_xlabel('Dias')
    f_ax0.bar(x, data[0])
    f_ax0.plot(x_s, data_s[0], 'r-')

    #Plota dados da figura 1
    f_ax1 = fig.add_subplot(gs[0,1])
    f_ax1.set_title('Casos novos - ' + state)
    f_ax1.set_ylabel('Novos casos')
    f_ax1.set_xlabel('Dias')
    f_ax1.bar(x, data[1])
    f_ax1.plot(x_s, data_s[1], 'r-')

    #Plota dados da figura 2
    f_ax2 = fig.add_subplot(gs[1:,0:])
    f_ax2.set_title('r0 aproximado - ' + state)
    f_ax2.set_ylabel('r0')
    f_ax2.set_xlabel('Dias')
    #f_ax2.plot(x_r0, data_r0[0], 'r--')
    #f_ax2.plot(x_r0, data_r0[1], 'r--')
    f_ax2.plot(x_r0, data_r0[2], 'r-')

    #plt.show()

    export_file = 'dados_r0/' + state + '_r0-aprox.svg' #Nome do arquivo de saida
    plt.savefig(export_file)
    
    plt.close()


#criando um arquivo .csv com o r0
def export_data(state, r0_max, r0_min, r0_aprox):
    export_file = 'dados_r0/' + state + '_r0.csv' #Nome do arquivo de saida
    with open(export_file, 'w', newline='') as file:
        writer = csv.writer(file) #Cria objeto de escrita
        writer.writerow(["r0_max", "r0_min", "r0_aprox"]) #Escreve o nome das colunas
        for i in range(0,len(r0_max)):
            row = [r0_max[i],r0_min[i],r0_aprox[i]] #Formata entradas da linha
    
            writer.writerow(row) #Escreve linha

def main(state_list):
    n = 3
    cycles = 4
    for state in state_list:
        C, dC, C_s, dC_s, d2C_s = import_data(state,n,cycles)
        r0_max, r0_min, r0_aprox = generate_data(N[state],C_s,dC_s,d2C_s)
        plot_graphs(state, [C,dC], [C_s,dC_s,d2C_s], [r0_max,r0_min,r0_aprox])
        export_data(state,r0_max,r0_min,r0_aprox)
        print(state, "OK!")

if __name__ == "__main__":
    argv = sys.argv[1:]
    if argv == [] or argv[0].lower() == '-h':
        print("""Use:
python analise_r0.py -h                                 --show this help message
python analise_r0.py -a                                 --run all
python analise_r0.py <state1> <state2> ... <stateN>     --run only states in list""")
    elif argv[0].lower() == '-a':
        main( list(N.keys()) )
    else:
        main(argv)
