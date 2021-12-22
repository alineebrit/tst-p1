numero = int(input())
if numero < 3 or numero == 3:
    valor = (numero * 0.5) + 1
    print(f"R$ {valor:.2f}")
else: 
    blocos = numero // 5
    resto = numero % 5
    valor2 = ((resto * 0.7) + (blocos * 3)) + 1
    print(f"R$ {valor2:.2f}")

