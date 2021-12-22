n1 = int(input())
n2 = int(input())
n3 = int(input())
modulo1 = abs(n1)
modulo2 = abs(n2)
modulo3 = abs(n3)
divisao1 = modulo1 // 11
resto1 = modulo1 % 11
divisao2 = modulo2 // 11
resto2 = modulo2 % 11
divisao3 = modulo3 // 11
resto3 = modulo3 % 11
print(f"{resto1:0>2}-{resto2:0>2}-{resto3:0>2}")

