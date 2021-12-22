cont = 0
saldo = 0
media = 0

while True:

    valor = float(input())
    if valor < media: break
    cont += 1
    saldo += valor
    media = saldo/cont

print(f"Saldo total do FIS: R${saldo:.2f}.")
print(f"Média das contribuições: R${(media):.2f}.")
