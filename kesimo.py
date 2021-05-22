# -*- coding: utf-8 -*-
import random
import numpy
import math
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import arange

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
	
	#ListaDecrescente = list(reversed(range(0, h+2)))
	ListaCrescente = list(range(0, h+2))

	TempoInicio = time.time()
	
	#direita = len(ListaDecrescente)-1
	#print(ListaDecrescente)
	#kesimo(ListaDecrescente,0,direita, (direita)/2)
	#print(ListaDecrescente)
	
		
	direita = len(ListaCrescente)-1 	
	#print(ListaCrescente)
	kesimo(ListaCrescente,0,direita, (direita)/2)
	#print(ListaCrescente)
	
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





