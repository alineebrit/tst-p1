binario = input()
tamanho = len(binario)
decimal = 0
for i in binario:
	elev = 2**(tamanho-1)
	a = int(i) * elev
	print(f"{int(i)} * {elev} = {a}")
	tamanho -= 1
	decimal += a
print(f"{binario}(2) = {decimal}(10)")
