print("Cálculo da Superfície de um Cilindro")
print("---")
import math
diametro = float(input("Medida do diâmetro? "))
altura = float(input("Medida da altura? "))
raio = diametro / 2
area_lateral = 2 * math.pi * raio * altura
area_base = 2 * math.pi * (raio **2)
area_total = area_lateral + area_base 
print(f"---")
print(f"Área calculada: {area_total:.2f}")

