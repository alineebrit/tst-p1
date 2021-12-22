contador_peso = 0
contador_combustivel = 0
contador_altitude = 0

while True:
    dados = input().split()
    peso = int(dados[0])
    combustivel = int(dados[1])
    altitude = int(dados[2])
    if peso < 0:
        print(f"dado inconsistente. peso negativo.")
        break
    elif combustivel < 0:
        contador_peso += 1
        print(f"dado inconsistente. combustível negativo.")
        break
    elif altitude < 0:
        contador_peso += 1
        contador_combustivel += 1
        print(f"dado inconsistente. altitude negativa.")
        break
    else:
        contador_peso += 1
        contador_combustivel += 1
        contador_altitude += 1

print(f"peso: {contador_peso}")
print(f"combustível: {contador_combustivel}")
print(f"altitude: {contador_altitude}")
