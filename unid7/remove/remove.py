def remove_divisores_k(lista, k, n):
  contador = 0
  for i in range(len(lista) -1, -1, -1):
    if k % lista[i] == 0 and k != 0 and lista[i] != 0:
        if contador == n: break
        lista.pop(i)
        contador+= 1
    
