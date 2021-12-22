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
print(f"Alimentacao: R$ {alimentacao}")
print(f"Cinema: R$ {cinema}")
print(f"Custo médio por pessoa: R$ {por_pessoa}")
print(f"Total: {total}")
print(f"Saldo após passeio: {saldo}")
