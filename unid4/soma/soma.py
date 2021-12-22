referencia = int(input())
soma = 0 
for a in range(10):
    numero = int(input()) 
    if referencia % numero == 0:
        soma += numero

print(f"{soma}")


