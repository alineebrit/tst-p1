
nome = input("Nome? ")
valor_da_letra = float(input("Valor da letra(R$)? "))
letra = len(nome)
preco_final = valor_da_letra * letra
print(f"Preço final: (R$) {preco_final:.2f}")
