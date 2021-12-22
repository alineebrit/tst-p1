valores = []
tamanhos = []
confortos = []
hoteis = []

while True:
    dados = input().split(",")
    if dados[0] == "---":
        break
    valores.append(float(dados[0]))
    tamanhos.append(int(dados[1]))
    confortos.append(int(dados[2]))
    hoteis.append(dados[3])

hotel_valor = hoteis[0]
valor_final = valores[0]
for v in range(1, len(valores)):
    if valor_final > valores[v]:
        valor_final = valores[v]
        hotel_valor = hoteis[v]


hotel_tamanho = hoteis[0]
tamanho_final = tamanhos[0]
for t in range(1, len(tamanhos)):
    if tamanho_final < tamanhos[t]:
        tamanho_final = tamanhos[t]
        hotel_tamanho = hoteis[t]

hotel_conforto = hoteis[0]
conforto_final = confortos[0]
for a in range(1, len(confortos)):
    if conforto_final < confortos[a]:
        conforto_final = confortos[a]
        hotel_conforto = hoteis[a]

while True:
    acao = input()
    if acao == "fim":
        break
    elif acao == "valor":
        print(f"{hotel_valor}")
    elif acao == "tamanho":
        print(f"{hotel_tamanho}")
    elif acao == "conforto":
        print(f"{hotel_conforto}")
