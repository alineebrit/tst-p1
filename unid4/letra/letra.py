palavra1 = input()
palavra2 = input()
index = 0
soma = 0
tamanho = len(palavra1) + len(palavra2)
print("Letras coincidentes")
for i in range(len(palavra1)):
    index += 1
    if (palavra1[i] == palavra2[i]):
        print(f"'{palavra1[i]}' na posição {index}")
        soma += 1
porcentagem = ((soma * 100) / (tamanho))
print(f"Total de letras coincidentes: {soma} ({porcentagem:.0f}%)")

