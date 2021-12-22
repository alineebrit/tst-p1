sequencia = []
tamanho = 0
palavras = 0

while True:

  palavra = input()

  if palavra == "fim":
    break

  sequencia.append(palavra)
  tamanho += len(palavra)
  palavras += 1

media = tamanho / palavras
print(f"{media:.2f}")

for e in range(len(sequencia)):

  if len(sequencia[e]) > media:
    print(f"{e+1} {sequencia[e]}")
