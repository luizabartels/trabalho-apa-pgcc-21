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
		particao = M1 (L, L_0, L_n)
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

EixoTempoCrescente = []
EixoTempoSemi = []
EixoTempoDecrescente = []
EixoNumeroEntrada = []
EixoNN = []
EixoNLog = []
xlim = 0
x = []

EixoNumeroEntradaC = []
EixoTempoC = []
xteste = []

def AjusteQuadratico(x, a):
	return a * x * x

def AjusteLogaritmico(x, a):
	return a * numpy.log(a * x)


for h in range (1, 2000):
	EixoNumeroEntrada.append(h)

	# Melhor caso
	TempoInicioCrescente = time.time()
	QuickSort(range(0, h+1))
	TempoFinalCrescente = time.time() - TempoInicioCrescente
	EixoTempoCrescente.append(TempoFinalCrescente)
	
	# Médio caso
	TempoInicioSemi = time.time()
	QuickSort(list(random.sample(range(0, h), h-1)))
	TempoFinalSemi = time.time() - TempoInicioSemi
	EixoTempoSemi.append(TempoFinalSemi)

	# Pior caso
	TempoInicioDecrescente = time.time()
	QuickSort(list(reversed(range(0, h+1))))
	TempoFinalDecrescente = time.time() - TempoInicioDecrescente
	EixoTempoDecrescente.append(TempoFinalDecrescente)

	xlim = h

	


poptQuadratico, _ = curve_fit(AjusteQuadratico, EixoNumeroEntrada, EixoTempoDecrescente)
a = poptQuadratico
xQuadratico = arange(min(EixoNumeroEntrada), max(EixoNumeroEntrada), 1)
yQuadratico = AjusteQuadratico(xQuadratico, a)


poptLogaritmico, _ = curve_fit(AjusteLogaritmico, EixoNumeroEntrada, EixoTempoCrescente)
d = poptLogaritmico
print "d, e, f: ", d
xLogaritmico = arange(min(EixoNumeroEntrada), max(EixoNumeroEntrada), 1)
yLogaritmico = AjusteLogaritmico(xLogaritmico, d)

poptLogaritmico1, _ = curve_fit(AjusteLogaritmico, EixoNumeroEntrada, EixoTempoSemi)
g = poptLogaritmico1
print "d, e, f: ", g
xLogaritmico1 = arange(min(EixoNumeroEntrada), max(EixoNumeroEntrada), 1)
yLogaritmico1 = AjusteLogaritmico(xLogaritmico1, g)



PegaListaMax = []
PegaListaMax.append(EixoTempoCrescente)
PegaListaMax.append(EixoTempoSemi)
PegaListaMax.append(EixoTempoDecrescente)
EixoMax = []
EixoMax = max(PegaListaMax, key=max)

plt.xlim(0, xlim)
plt.ylim(0, max(EixoMax))
plt.plot(EixoNumeroEntrada, EixoTempoCrescente, color='black')
#plt.plot(EixoNumeroEntrada, EixoTempoSemi, color='green')
plt.plot(EixoNumeroEntrada, EixoTempoDecrescente, color='pink')
plt.plot(xQuadratico, yQuadratico,  linewidth=5, color='red')
#plt.plot(xLogaritmico, yLogaritmico,  linewidth=5, color='orange')
#plt.plot(xLogaritmico1, yLogaritmico1,  linewidth=5, color='blue')

# Fit 
coefficients = numpy.polyfit(EixoNumeroEntrada*numpy.log(EixoNumeroEntrada),EixoTempoCrescente,1) # Use log(x) as the inumpyut to polyfit.
fit = numpy.poly1d(coefficients) 

coefficients1 = numpy.polyfit(EixoNumeroEntrada*numpy.log(EixoNumeroEntrada),EixoTempoDecrescente,1)
fit1 = numpy.poly1d(coefficients1) 

prod = []

for i in range(0, len(EixoNumeroEntrada)):
	prod.append(EixoNumeroEntrada[i]*EixoNumeroEntrada[i])

plt.plot(EixoNumeroEntrada,fit(EixoNumeroEntrada*numpy.log(EixoNumeroEntrada)),"--", label="fit")
plt.plot(EixoNumeroEntrada,fit(EixoNumeroEntrada*numpy.log(EixoNumeroEntrada)),"--", color = 'red')

plt.show()





