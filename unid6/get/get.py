def get_items(valores, indices):
    lista_nova = []
    for e in indices:
        if e < len(valores):
            lista_nova.append(valores[e])
        else:
            lista_nova.append(None)
    return lista_nova




valores = [18, 22, 73, 32, 19, 21, 43]
indices = [3, 4, 8, 1]
assert get_items(valores, indices) == [32, 19, None, 22]
