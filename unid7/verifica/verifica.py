def verifica_esteira(esteira, componentes):
  lista_vazia = []
  for a in range(len(esteira)):
    for i in range(len(componentes)):
        if esteira[a] == componentes[i]:
            lista_vazia.append(esteira[a])
  if lista_vazia == componentes:
    return True
  else:
    return False

