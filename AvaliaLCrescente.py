# -*- coding: utf-8 -*-
import random
import numpy
import math
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import arange

def QuickSortM1(L, L_0 = 0, L_n = None):

	if L_n is None:
		L_n = len(L) - 1

	if L_0 < L_n:
		particao = M1 (L, L_0, L_n)
		QuickSortM1(L, L_0, particao-1)
		QuickSortM1(L, particao+1, L_n)

def QuickSortM2(L, L_0 = 0, L_n = None):

	if L_n is None:
		L_n = len(L) - 1

	if L_0 < L_n:
		particao = M2 (L, L_0, L_n)
		QuickSortM2(L, L_0, particao-1)
		QuickSortM2(L, particao+1, L_n)

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

##############################################################################
# 3 - AchaPivo																 #
##############################################################################

def achaPivo (vetor, esquerda, direita):
  pivo = 0;
  pos = esquerda + 1

  while pos <= direita:
    if vetor[pos] >= vetor[pos-1]: 
      pos+=1
    else:
      pivo = pos
      pos = direita + 1

  return pivo

def particao (vetor, esquerda, direita, pivo):
  #while esquerda <= direita:
  while vetor[esquerda] < pivo:
    esquerda+=1
  while vetor[direita] > pivo:
    direita-=1
  if esquerda <= direita:
    troca = vetor[esquerda]
    vetor[esquerda] = vetor[direita]
    vetor[direita] = troca
    esquerda+=1
    direita-=1
  return direita

def quickSort(vetor, esquerda, direita):
  pivo = achaPivo(vetor,esquerda, direita)
  #print(pivo)
  if pivo != 0:
    p = particao(vetor, esquerda, direita, vetor[pivo-1])
    quickSort(vetor, esquerda, p)
    quickSort(vetor, p+1, direita)

##############################################################################
# 3 - Kesimo																 #
##############################################################################

def kesimo(vetor,esquerda,direita,k):
  if esquerda < direita:
    pivo = achaPivo(vetor, esquerda, direita)  
    p = particao(vetor, esquerda, direita, vetor[pivo-1]) 
    
    if pivo!=0:     
      if(p >= k):
        kesimo(vetor, esquerda, p , k)
      elif(p < k):
        kesimo(vetor, p+1, direita , k)


###################################
### Níveis de desordem da lista ###
###################################

def EscolheLista(Nivel, IteracaoMax):
	if Nivel == "crescente": # Melhor caso
		return range(0, IteracaoMax)
	elif Nivel == "semi": # Médio caso
		return list(random.sample(range(0, IteracaoMax), IteracaoMax-1))
	elif Nivel == "decrescente": # Pior Caso
		return list(reversed(range(0, IteracaoMax)))

EixoTempoM1 = []
EixoTempoM2 = []
EixoTempoAchaPivo = []
EixoTempoK = []

EixoNumeroEntrada = []

xlim = 0
x = []

EixoNumeroEntradaC = []
EixoTempoC = []
xteste = []

def AjusteQuadratico(x, a):
	return a * x * x

def AjusteLogaritmico(x, a):
	return a * numpy.log(a * x)


for h in range (1, 50000):
    EixoNumeroEntrada.append(h)
    ListaCrescente = range(0, h+1) # Melhor caso
    ListaSemiOrdenada = list(random.sample(range(0, h+1), h)) # Caso médio
    ListaDecrescente = list(reversed(range(0, h+1))) # Pior caso


	# Randômico
    TempoInicioM1 = time.time()
    QuickSortM1(ListaCrescente)
    TempoFinalM1 = time.time() - TempoInicioM1
    EixoTempoM1.append(TempoFinalM1)
	
	# Indexado
    TempoInicioM2 = time.time()
    QuickSortM2(ListaCrescente)
    TempoFinalM2 = time.time() - TempoInicioM2
    EixoTempoM2.append(TempoFinalM2)

    # AchaPivo
    TempoInicioAchaPivo = time.time()
    quickSort(ListaCrescente,0,len(ListaCrescente)-1)
    TempoFinalAchaPivo = time.time() - TempoInicioAchaPivo
    EixoTempoAchaPivo.append(TempoFinalAchaPivo)

    #Kesimo
    TempoInicioK = time.time()
    direita = len(ListaCrescente)-1 	
    kesimo(ListaCrescente,0,direita, (direita)/2)
    TempoFinalK = time.time() - TempoInicioK
    EixoTempoK.append(TempoFinalK)

    xlim = h


PegaListaMax = []
PegaListaMax.append(EixoTempoM1)
PegaListaMax.append(EixoTempoM2)
EixoMax = []
EixoMax = max(PegaListaMax, key=max)

plt.xlim(0, xlim)
plt.ylim(0, max(EixoMax))
plt.xlabel("Numero de Entradas - n")
plt.ylabel("Tempo de Execucao - t")
plt.grid()
#plt.plot(EixoNumeroEntrada, EixoTempoM1, color='black')
#plt.plot(EixoNumeroEntrada, EixoTempoM2, color='pink')
#plt.plot(EixoNumeroEntrada, EixoTempoAchaPivo, color='green')
#plt.plot(EixoNumeroEntrada, EixoTempoK, color='blue')

# Fit M1
coefficientsM1 = numpy.polyfit(EixoNumeroEntrada*numpy.log(EixoNumeroEntrada),EixoTempoM1,1)
fitM1 = numpy.poly1d(coefficientsM1) 
# Fit M2
coefficientsM2 = numpy.polyfit(EixoNumeroEntrada*numpy.log(EixoNumeroEntrada),EixoTempoM2,1)
fitM2 = numpy.poly1d(coefficientsM2)
# Fit AchaPivo
coefficientsAchaPivo = numpy.polyfit(EixoNumeroEntrada*numpy.log(EixoNumeroEntrada),EixoTempoAchaPivo,1)
fitAchaPivo = numpy.poly1d(coefficientsAchaPivo) 
# Fit Kesimo
coefficientsK = numpy.polyfit(EixoNumeroEntrada*numpy.log(EixoNumeroEntrada),EixoTempoK,1)
fitK = numpy.poly1d(coefficientsK) 


plt.plot(EixoNumeroEntrada,fitM1(EixoNumeroEntrada*numpy.log(EixoNumeroEntrada)), label= 'Randomico')
plt.plot(EixoNumeroEntrada,fitM2(EixoNumeroEntrada*numpy.log(EixoNumeroEntrada)), label = 'Indexado')
plt.plot(EixoNumeroEntrada,fitAchaPivo(EixoNumeroEntrada*numpy.log(EixoNumeroEntrada)), label = 'AchaPivo')
plt.plot(EixoNumeroEntrada,fitK(EixoNumeroEntrada*numpy.log(EixoNumeroEntrada)), label = 'Kesimo')

plt.title("Melhor Caso - Lista crescente - (Ajuste de curva para nlog(n))")
plt.legend(loc = "upper left")
plt.show()