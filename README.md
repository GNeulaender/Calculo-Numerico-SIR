# Calculo-Numerico-SIR
Uso do modelo SIR para modelagem da epidemia do COVID-19 no Brasil.

O relatório final do grupo sobre o trabalho se encontra [aqui](relatorio/relatorio.pdf).

## Membros do Grupo
- Guido Neulaender
- Heloisa Pimentel
- Silas Leonel
- Rodrigo Ryan
- João Francisco

## Organização do Repositório
- [analise_r0.py](analise_r0.py) faz as suavisações dos dados, calcula a sequência de r0 por tempo e exporta dos dados para [dados_r0](dados_r0).
- [constantes.py](constantes.py) possui uma lista de valores fixos usados em vários códigos.
- [plot_simulation.py](plot_simulation.py) plota os gráficos da simulação em MG, tanto para r0 fixo quando variável e salva os resultados em [simulacoes](simulacoes).
- [runge_kutta.py](runge_kutta.py) é a implementação do método de Runge-Kutta de quarta ordem em Python.

## Alguns dados preliminares
### Brasil
![Dados preliminares do Brasil](/dados_r0/BR_r0-aprox.svg)
### São Paulo
![Dados preliminares de São Paulo](/dados_r0/SP_r0-aprox.svg)
### Minas Gerais
![Dados preliminares de Minas Gerais](/dados_r0/MG_r0-aprox.svg)

## Simulações para Minas Gerais (MG)
### r0 = 2.6 fixo
![Simulação do r0 fixo na epidemia de Minas Gerais](/simulacoes/SimulacaoA_r0fixo.svg)
### r0 como função do tempo
![Simulação do r0(t) na epidemia de Minas Gerais](/simulacoes/SimulacaoB_r0variavel.svg)
