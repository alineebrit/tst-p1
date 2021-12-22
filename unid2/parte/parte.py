n1 = float(input())
n2 = float(input())
n3 = float(input())

soma = n1 + n2 + n3
valor_int = soma // 1
valor_dec = soma % 1

print(f"Soma: {soma:.2f}")
print(f"Parte Inteira: {valor_int:.0f}")
print(f"Parte Decimal: {valor_dec:.2f}")
