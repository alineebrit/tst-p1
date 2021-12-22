k = int(input())
contador = 0
n = int(input())
lista = []

for a in range(n):
	numero = int(input())
	lista.append(numero)
for a in lista:
	if a % k == 0:
		contador += 1
	percentual = (100 * contador) / len(lista)
print(f"{contador} ({percentual:.1f}%)")
