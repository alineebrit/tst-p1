def insere_ordenado_ultimo(lista):
    for i in range(len(lista) -1, 0, -1):
        if lista[i] < lista[i - 1]:
            lista[i], lista[i - 1] = lista[i - 1], lista[i]
