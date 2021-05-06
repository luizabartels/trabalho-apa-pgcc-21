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
  while esquerda <= direita:
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
  pivo = achaPivo(vetor, 0, len(vetor) -1)
  if pivo != 0:
    p = particao(vetor, esquerda, direita, vetor[pivo-1])
    quickSort(vetor, esquerda, p)
    quickSort(vetor, p+1, direita)


vetor = [100, 89, 76, 65, 65, 15, 8, 6, 4, 3]
print(vetor)
quickSort(vetor, 0, len(vetor) -1)
print(vetor)

