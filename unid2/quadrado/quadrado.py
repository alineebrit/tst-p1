raio = float(input())
import math
circulo = ((raio ** 2) * math.pi)
quadrado = (2 * (raio**2))
diferenca = circulo - quadrado

print(f"Área não comum: {diferenca:.5f}")


