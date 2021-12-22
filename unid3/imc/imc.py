peso = float(input())
altura = float(input())

calculo = (peso / (altura **2))
print(f"IMC = {calculo:.1f}")
if calculo < 18.5:
	print("Classificação = Magreza")
elif 18.5 <= calculo < 25:
	print("Classificação = Saudável")
elif 25 <= calculo < 30:
	print("Classificação = Sobrepeso")
elif calculo >= 30:
	print("Classificação = Obesidade")
