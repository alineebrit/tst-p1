def distribui_materia_prima(esteira_de_materia_prima, n):
    lista_vazia = []
    for a in range(n):
        lista_vazia.append([])
    indice = 0
    while True:
        if indice >= len(esteira_de_materia_prima): break
        for i in range(len(lista_vazia)):
            lista_vazia[i].append(esteira_de_materia_prima[indice])
            indice += 1
            if indice >= len(esteira_de_materia_prima): break

    return lista_vazia


