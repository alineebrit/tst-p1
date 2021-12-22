orcamento = float(input("Orçamento? R$ "))
num_adultos = int(input("Número de adultos? "))
num_criancas = int(input("Número de crianças? "))
pizza = float(input("Preço da pizza? R$ "))
refrigerante = float(input("Preço do refrigerante? R$ "))
estacionamento = float(input("Preço do estacionamento? R$ "))
ingresso = float(input("Preço do ingresso do cinema? R$ "))

alimentacao = pizza + refrigerante
adultos = num_adultos * ingresso + 2
criancas = num_criancas * ingresso + 2 / 2
cinema = adultos + criancas
por_pessoa = cinema + alimentacao + estacionamento / adultos + criancas
total = alimentacao + cinema + estacionamento
saldo = orcamento - total

print("========== Despesas do cinema ==========")
print(f"Alimentacao: R$ {alimentacao:.2f}")
print(f"Cinema: R$ {cinema:.2f}")
print(f"Custo médio por pessoa: R$ {por_pessoa:.2f}")
print(f"Total: {total:.2f}")
print(f"Saldo após passeio: {saldo:.2f}")
