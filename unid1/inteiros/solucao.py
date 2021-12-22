# Programa que efetua operações utilizando o módulo de x

x = int(input())

modulo = abs(x)
modulo_menos_2 = (abs(x) - 2)
metade = modulo // 2

print(f"Para x = {x}")
print("---")
print(f"|x| = {modulo}")
print(f"|x - 2| = {modulo_menos_2}")
print(f"|x / 2| = {metade:.2f}")
          
