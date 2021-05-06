# -*- coding: utf-8 -*-
import random
import numpy
import math
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import arange

def QuickSort(L, L_0 = 0, L_n = None):

	if L_n is None:
		L_n = len(L) - 1

	if L_0 < L_n:
		particao = M2 (L, L_0, L_n)
		QuickSort(L, L_0, particao-1)
		QuickSort(L, particao+1, L_n)

#################################
### Opções de escolha do pivo ###
#################################

############
# 0 - Base #
############

def M0 (L, L_0, L_n):

	pivo = L[L_n]
	i = L_0

	for j in range(L_0, L_n):
		if L[j] <= pivo:
			L[j], L[i] = L[i], L[j]
			i = i + 1
	L[i], L[L_n] = L[L_n], L[i]

	return i

#############################################################################################
# 1 - Randômico com distribuição uniforme, Prob{pivô= L[i] }= 1/(n2-n1 +1)  para i=n1,...,n2#
#############################################################################################

def M1 (L, L_0, L_n):

	x = int(math.floor(numpy.random.uniform(L_0, L_n)))
	pivo = x

	L[L_n], L[pivo] = L[pivo], L[L_n]
	return M0(L, L_0, L_n)

##############################################################################
# 2 - Indexado como  média de 3 valores:  (L[n1] + L[n2] + L[(n1+n2)DIV2])/3 #
##############################################################################

def M2 (L, L_0, L_n): ### Atenção: selecionar índice que esteja dentro da partição
	
	n1_indice = random.randrange(L_0,L_n) # Seleciona indice qualquer na lista.
	n2_indice = random.randrange(L_0,L_n) # Seleciona indice qualquer na lista.

	n1 = L[n1_indice] # Descobre valor n1.
	n2 = L[n2_indice] # Descobre valor n2.	
	n3_indice = (n1_indice + n2_indice)//2 # Considera n3 como sendo o quociente da divisão por 2 da soma dos índices n1 e n2.
	n3 = L[n3_indice]

	pivo = ((n1 + n2 + n3) / 3) # Descobre o índice do pivo. Como todos os valores são inteiros, a divisão será inteira.

	L[L_n], L[pivo] = L[pivo], L[L_n]
	return M0(L, L_0, L_n)

#########################################################
# 3 - Utilizando o algoritmo AchaPivo das notas de aula #
#########################################################

#def M3 (L, L_0, L_n):

#####################################
# 4 - Utilizando a mediana da lista #
#####################################

#def M3 (L, L_0, L_n):

###################################
### Níveis de desordem da lista ###
###################################

ListaCrescente = range(0, 11) # Melhor caso
# print ListaCrescente
ListaSemiOrdenada = list(random.sample(range(0, 11), 10)) # Caso médio
# print ListaSemiOrdenada
ListaDecrescente = list(reversed(range(0, 11))) # Pior caso
# print ListaDecrescente


EixoTempo = []
EixoNumeroEntrada = []
EixoNN = []
EixoNLog = []
xlim = 0
x = []

EixoNumeroEntradaC = []
EixoTempoC = []

def AjusteQuadratico(x, a, b, c):
	return a * x * x + b * x + c

for h in range (1, 5000):
	
	ListaDecrescente = list(reversed(range(0, h+2)))

	TempoInicio = time.time()
	QuickSort(ListaDecrescente)
	TempoFinal = time.time() - TempoInicio

	EixoTempo.append(TempoFinal)
	EixoNumeroEntrada.append(h)


	#ListaCrescente = range(0, 11)
	
	#TempoInicioC = time.time()
	#QuickSort(ListaCrescente)
	#TempoFinalC = time.time() - TempoInicioC

	#EixoTempoC.append(TempoFinalC)
	#EixoNumeroEntradaC.append(h)

	#EixoNN.append(h * h)
	#EixoNLog.append(h * math.log(h))

	#print "Tempo de execução: ", TempoFinal
	xlim = h

popt, _ = curve_fit(AjusteQuadratico, EixoNumeroEntrada, EixoTempo)
a, b, c = popt
x = arange(min(EixoNumeroEntrada), max(EixoNumeroEntrada), 1)
y = AjusteQuadratico(x, a, b, c)
#print "Lista ordenada: ", ListaDecrescente

plt.xlim(0, xlim)
plt.ylim(0, max(EixoTempo))
plt.scatter(EixoNumeroEntrada, EixoTempo, color='black')
plt.plot(x, y, '--',  linewidth=5, color='red')
#plt.scatter(EixoNumeroEntradaC, EixoTempoC, color='red')
#plt.plot(EixoNumeroEntrada, EixoNN)
#plt.plot(EixoNumeroEntrada, EixoNLog)
plt.show()





