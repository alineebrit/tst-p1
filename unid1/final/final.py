print("== Estágio 1 ==")
peso_1 = float(input("Peso? "))
nota_1 = float(input("Nota? "))

print("== Estágio 2 ==")
peso_2 = float(input("Peso? "))
nota_2 = float(input("Nota? "))

print("== Estágio 3 ==")
peso_3 = float(input("Peso? "))
nota_3 = float(input("Nota? "))

media_parcial = (nota_1*peso_1) + (nota_2*peso_2)+ (nota_3*peso_3)
media_5 = ((5-(media_parcial*0.6)))/0.4
media_7 = ((7-(media_parcial*0.6)))/0.4

print("== Resultados ==")
print(f"Média parcial: {media_parcial:.1f}")
print(f"Nota na final, pra média 5.0 = {media_5:.1f}")
print(f"Nota na final, pra média 7.0 = {media_7:.1f}")
