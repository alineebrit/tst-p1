razao = int(input())
contador = 0

while True:
    sequencias = input()

    if sequencias == 'fim':
        break

    sequencias = sequencias.split()

    pa = 0

    for i in range(len(sequencias)- 1):
        if (int(sequencias[i + 1]) - int(sequencias[i])) == razao:
          pa += 1
    if pa == len(sequencias) - 1:
        contador += 1


print(f"{contador}")
