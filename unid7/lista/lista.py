def meu_in(elemento, lista):
    for e in lista:
        if e == elemento:
            return True
    return False


def lista_so_com_oposto(lista):
    for i in range(len(lista) - 1, -1, -1):
        if meu_in(lista[i] * -1, lista) == False:
            lista.pop(i)


lista1 = [1, 2, 1, 3, 4, -1, -3, 5]
lista_so_com_oposto(lista1)
assert lista_so_com_oposto(lista1) == None
assert lista1 == [1, 1, 3, -1, -3]
