numero = int(input())
soma = 0 
contador1= 0 
media = 0
cont2 = 0
lista = []
for i in range(numero):
	n = int(input())
	lista.append(n)
	if n % 2 == 0:
		contador1 += 1
		soma += n 
		media = soma / contador1
	
for i in lista:
	if i < media:
		cont2 +=1

print(f"soma: {soma}")
print(f"média: {media:.1f}")
print(f"{cont2} número(s) abaixo da média")

