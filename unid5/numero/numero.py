num = abs(int(input()))

digitos = 1
while num >= 10:
  num = num // 10

  digitos += 1

print(digitos)
