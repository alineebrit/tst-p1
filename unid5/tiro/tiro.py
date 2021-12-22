import math

soma = 0
cont = 0

while True:
    distancia = input().split()
    d1 = float(distancia[0])
    d2 = float(distancia[1])
    d_final = math.sqrt((d1 ** 2) + (d2 ** 2))
    if float(d_final) > 200 or float(d_final) > 200: break
    print(f"{d_final:.2f}cm")
    soma += d_final
    cont += 1

print("--")
print(f"num disparos: {cont}")
print(f"distancia media: {(soma/cont):.2f}cm")
