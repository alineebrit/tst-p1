def seleciona_perfeitos(lista):

    perfeitos = []

    for e in lista:

        contador = 0
        for i in range(1, e):

            if e % i == 0:

                contador += i
        if contador == e:

            perfeitos.append(e)
    return perfeitos

lista = [3, 6, 9, 12, 15, 18, 19, 21, 28]
assert seleciona_perfeitos(lista) == [6, 28]
assert lista == [3, 6, 9, 12, 15, 18, 19, 21, 28]
