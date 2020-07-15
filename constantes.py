import numpy as np

gamma = 0.14 #Constante gamma fornecida pelo professor
state = 'MG' #Estado escolhido para plotagem

#Habitantes por estado segundo o IBGE de 2019
N = {
	'BR': 210147125,
	'AC': 881935,
	'AL': 3337357,
	'AP': 845731,
	'AM': 4144597,
	'BA': 14873064,
	'CE': 9132078,
	'DF': 3015268,
	'ES': 4018650,
	'GO': 7018354,
	'MA': 7075181,
	'MT': 3484466,
	'MS': 2778986,
	'MG': 21168791,
	'PA': 8602865,
	'PB': 4018127,
	'PR': 11433957,
	'PE': 9557071,
	'PI': 3273227,
	'RJ': 17264943,
	'RN': 3506853,
	'RS': 11377239,
	'RO': 1777225,
	'RR': 605761,
	'SC': 7164788,
	'SP': 45919049,
	'SE': 2298696,
	'TO': 1572866
}
#Fonte:
#ftp://ftp.ibge.gov.br/Estimativas_de_Populacao/Estimativas_2019/estimativa_dou_2019.xls
# ou
#https://ibge.gov.br/Estimativas_de_Populacao/Estimativas_2019

r0_fixo = lambda t: 2.6 #Aproximação fixa do r0 baseada nos dados da China
r0_funcao = lambda t: 1.282 + 3.5658*np.exp(-t/7.80892) #Aproximação para função r0(t)
#Fonte: Dados calculados no Scidavis usando decaimento exponencial
#       y(x) = y0 + A*exp(-x/t)
#
#       A (amplitude) = 3,56575654128821 +/- 0,130614568183679
#       t (e-folding time) = 7,80915433580217 +/- 0,00683524788389776
#       y0 (offset) = 1,28199812621955 +/- 0,0185826754725847
