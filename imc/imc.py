#calcular o indice de massa corporal
altura = float(input("digite sua altura em metros "))
peso = float(input("digite sua altura em kg"))
imc = peso / altura**2
peso_ideal =(24.9*(altura**2))
peso_desejado = peso_ideal - peso
print(f"IMC atual = {imc:.2f}")
print(f"peso a ser ganho/perdido = {peso_desejado:.2f}")
