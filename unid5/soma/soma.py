contador = 0
media = 0
maior = 0
n = []

while True:

    num = int(input())
    n.append(num)

    contador += num

    if contador >= 999: break

media = contador / len(n)

for a in n:
    if a > media:
        maior += 1

print(contador)
print(f"{media:.2f}")
print(maior)
