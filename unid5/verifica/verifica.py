saques = int(input())
saldo = float(input())
saque = 0

while True:
    lista = input().split()
    if lista[0] == "depósito":
        if float(lista[1]) > 1000.00:
            print(f"Operação inválida: {lista[0]} {lista[1]}.")
            print(f"Seu saldo é R$ {saldo:.2f}.")
            break
        else:
            saldo += float(lista[1])
    if lista[0] == "saque":
        if saldo - float(lista[1]) < 0:
            print(f"Operação inválida: {lista[0]} {lista[1]}.")
            print(f"Seu saldo é R$ {saldo:.2f}.")
            break
        elif saques == saque:
            print(f"Operação inválida: {lista[0]} {lista[1]}.")
            print(f"Seu saldo é R$ {saldo:.2f}.")
            break
        else:
            saldo -= float(lista[1])
            saque += 1
