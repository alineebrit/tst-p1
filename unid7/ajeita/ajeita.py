def ajeita_lista(lista):
    for parte in lista:
        for i in range(len(lista) - 1):
            if lista[i] % 2 == 1 and lista[i + 1] % 2 == 0:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

            if lista[i] % 2 == 1 and lista[i + 1] % 2 == 1 and lista[i + 1] < lista[i]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

            if lista[i] % 2 == 0 and lista[i + 1] % 2 == 0 and lista[i + 1] > lista[i]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
