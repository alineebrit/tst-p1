def variacao_bubble(lista, inicio, fim):
    indice = fim - 1
    contador = 0
    if len(lista) > 0:
        delta = fim - inicio
        for i in range(inicio, fim):
            delta -= 2
            if len(lista) % 2 == 0 and delta <= 0: break
            if len(lista) % 2 != 0 and delta - 1<= 0: break
            if lista[i] > lista[indice]:
                lista[i], lista[indice] = lista[indice], lista[i]
                indice -= 1
                contador += 1

    return contador
