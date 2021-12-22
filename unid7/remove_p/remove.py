def meu_in(elemento, lista):
    for i in lista:
        if i == elemento:
            return True
    return False


def remove_palavras_com_maiusculas(lista):
    for i in range(len(lista) - 1, -1, -1):
        for letra in lista[i]:
            if meu_in(letra, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') == True:
                lista.pop(i)
                break
