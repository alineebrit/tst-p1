valor_atual = float(input("Valor atual? "))
novo_valor = float(input("Novo valor? "))
diferenca = novo_valor - valor_atual
porcentagem = (diferenca*100)/valor_atual
print(f"Reajuste de {porcentagem:.1f}%")

