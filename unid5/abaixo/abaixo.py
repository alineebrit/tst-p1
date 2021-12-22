soma = 0
media = 0
posicao = 0
lista = []

while True:
    dado = input()
    if dado == 'fim':break
    posicao += 1
    soma += int(dado)
    lista.append([posicao, int(dado)])

media = soma / posicao
print(f"{media:.2f}")

for i in lista:
    if i[1] < media:
        print(i[0], i[1])


