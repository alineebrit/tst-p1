def meu_in(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return True
    return False

def insere_nome(aluno1, duplas, aluno2):
  duplas.append(aluno1)
  apto = meu_in(duplas, aluno2)
  if apto == True:
    for i in range(len(duplas) - 1, -1, -1):
      if duplas [i - 1] != aluno2:
        duplas[i], duplas[i - 1] = duplas[i - 1], duplas[i]
      elif duplas [i - 1] == aluno2:
        duplas[i], duplas[i - 1] = duplas[i - 1], duplas[i]
        break



