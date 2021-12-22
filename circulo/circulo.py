# coding: utf-8
# Área e perímetro de um Círculo

import math
math.pi
diametro = int(input())
raio = diametro / 2
area = math.pi*raio**2
perimetro = 2*math.pi*raio
print(f"A: {area:.5f}")
print(f"P: {perimetro:.5f}")
