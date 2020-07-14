import sys
import csv
import numpy as np
from constantes import gamma
from habitantes_federacao import N

#Valores das constantes 'alpha'
alpha_max = 20
alpha_min = 10

#Declaração de mi(t)
mi = lambda alpha, N, C, dC: (alpha/(gamma*N)) * (gamma*C + dC)
#Declaração de r0(t)
r0 = lambda alpha, N, C, dC, d2C: (1/(1-mi(alpha,N,C,dC))) + (d2C/(gamma*dC*(1-mi(alpha,N,C,dC)) ))

#Função de suavisação dos dados de casos novos
def smoother(C, n):
    Cs = C[2*n:] #Primeira soma (caso 'i=-n')
    for i in range(-n+1,n+1): #Somatoria de 'i=-n+1' a 'n'
        Cs += C[n-i:-(n+i)]
    return Cs/(2*n+1) #Média simples dos '2n+1' termos

#Importa dados do estado 'state' com suavisação 'n'
def import_data(state, n):
    input_file = 'data/' + state + '.csv' #Nome do arquivo de entrada
    C = np.genfromtxt(input_file, delimiter=',', usecols = (1)) #Importa dados dos casos acumulados
    Cs = smoother(C,n) #Suavisa dado dos casos acumulados
    dC = Cs[1:] - Cs[:-1] #Primeira derivada (casos novos) suavisada
    d2C = dC[1:] - dC[:-1] #Segunda derivada suavisada
    
    #Concatena arrays para terem a mesma dimensão
    Cs = Cs[2:]
    dC = dC[1:]

    return Cs, dC, d2C #Retorna dados formatados

def generate_data(N, Cs, dC, d2C):
    r0_max = r0(alpha_max, N, Cs, dC, d2C) #Calcula r0 máximo
    r0_min = r0(alpha_min, N, Cs, dC, d2C) #Calcula r0 mínimo
    r0_aprox = (r0_max + r0_min)/2 #Calcula melhor aproximação (média simples)

    return r0_max, r0_min, r0_aprox


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
    for state in state_list:
        Cs, dC, d2C = import_data(state,n)
        r0_max, r0_min, r0_aprox = generate_data(N[state],Cs,dC,d2C)
        export_data(state,r0_max,r0_min,r0_aprox)

if __name__ == "__main__":
    argv = sys.argv[1:]
    try:
        if argv == [] or argv[0].lower() == '-h':
            print("""Use:
python analise_r0.py -h                                 --show this help message
python analise_r0.py -a                                 --run all
python analise_r0.py <state1> <state2> ... <stateN>     --run only states in list""")
        elif argv[0].lower() == '-a':
            main( list(N.keys()) )
        else:
            main(argv)
    except:
        print("Error. Try checking state names?")
