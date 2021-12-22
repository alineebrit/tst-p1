tipo = input()

if tipo == "Caminhão":
    eixos = int(input())
    valor = 9.6 * eixos
    print(f"Valor a pagar: R$ {valor:.2f}.")
elif tipo == "Ônibus":
    eixos = int(input())
    valor = 11.4 * eixos
    print(f"Valor a pagar: R$ {valor:.2f}.")
elif tipo =="Automóvel utilitário":
    print("Valor a pagar: R$ 11.40.")
elif tipo == "Motocicleta":
    print("Valor a pagar: R$ 5.70.")
else:
    print("Veículo não cadastrado.")

