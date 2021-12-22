numero1 = float(input())
numero2 = float(input())
numero3 = float(input())

soma = numero1 + numero2 + numero3
valor_int = soma // 1
valor_dec = soma % 1

print(f"Soma: {soma:.2f}")
print(f"Parte Inteira: {valor_int:.0f}")
print(f"Parte Decimal: {valor_dec:.2f}")
