def meu_split(lista):
    aspas = ''
    split = []

    for letra in lista:
        if letra != " ":
            aspas += letra
        else:
            split.append(aspas)
            aspas = ''

    if aspas:
        split.append(aspas)

    #print(split)

    return split
def maior_palavra(frase):
    maior = 0
    lista_separada = meu_split(frase)
    for i in range(len(lista_separada)):
        if len(lista_separada[i]) >= len(lista_separada[maior]):
            maior = i
    return lista_separada[maior]

