def filtra_divisores(lista):
  
  for i in range(len(lista) -1, -1, -1):
    parte = str(lista[i])
    somatorio = 0
    for p in range(len(parte)):
        somatorio += int(parte[p])
    if lista[i] % somatorio != 0: 
        lista.pop(i)
