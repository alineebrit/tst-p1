contadorr = 0
razaoo = int(input())
while True:
    entrada = input()
    if entrada == 'fim': break
    pa = entrada.split()
    situacao = True
    for i in range(len(pa)-1):
        if int(pa[i]) + razaoo != int(pa[i+1]):
            situacao = False
            break
    if situacao == True:
        contadorr += 1

print(contadorr)
