def soma(entrada):
    soma = 0
    for a in entrada:
        soma += int(a)
    return soma

def subtracao(entrada):
    subtracao = int(entrada[0])
    for i in range(1, len(entrada)):
        subtracao -= int(entrada[i])
    return subtracao

def multiplicacao(entrada):
    multiplicador = 1
    for i in range(len(entrada)):
        multiplicaçao = int(entrada[i]) * multiplicador
        multiplicador = multiplicaçao 
    return multiplicaçao

def divisao(entrada):
    dividendo = int(entrada[0])
    for i in range(len(entrada) - 1):
        if int(entrada[i + 1]) == 0: return 'Erro: Divisão por 0'
        divisaov = dividendo // int(entrada[i + 1])
        dividendo = divisaov
    return divisaov
def meu_split(frase):
    aspas = ''
    splitt = []
    for letra in frase:
        if letra != " ":
            aspas += letra
        else:
            splitt.append(aspas)
            aspas = ''
    if aspas:
        splitt.append(aspas)
    return splitt

while True:
    parte = input()
    entrada = meu_split(parte)
    operacao = entrada.pop(0)
    if operacao == '5': break
    if operacao == '1': print(soma(entrada))
    if operacao == '2': print(subtracao(entrada))
    if operacao == '3': print(multiplicacao(entrada))
    if operacao == '4': print(divisao(entrada))
