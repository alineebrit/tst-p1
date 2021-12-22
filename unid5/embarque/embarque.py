embarque = input()
sequencia = embarque.split()
i = 0
impares = []
pares = []
total = []
while i < len(sequencia):

    if int(sequencia[i]) % 2 != 0:
        impares.append(sequencia[i])
    else:
        pares.append(sequencia[i])
    i += 1

total = impares+pares

if total == sequencia:
    print("ok")
else:
    print("erro")
