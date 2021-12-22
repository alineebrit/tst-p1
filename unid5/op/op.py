nome_saldo = input().split()
nome = nome_saldo[0]
soma = 0
soma += float(nome_saldo[1])
while True:
    entrada = input().split()

    if entrada[0] == '3':
        break
    elif entrada[0] == "1":
        soma -= float(entrada[1])
    elif entrada[0] == "2":
        soma += float(entrada[1])

print(f"Saldo de R$ {soma:.2f} na conta de {nome}")
    
