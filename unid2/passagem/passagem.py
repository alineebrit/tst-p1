distancia_em_milhas = float(input())
valor_da_aliquota = float(input())
valor_da_passagem = (distancia_em_milhas * valor_da_aliquota) + 51
a_vista = valor_da_passagem * (75/100)
em_6_parcelas = valor_da_passagem * (95/100)
parcelas_6 = em_6_parcelas / 6
parcelas_10 = valor_da_passagem / 10
print(f"Valor da passagem: R$ {valor_da_passagem:.2f}\n\nPagamento:\n1. À vista. R$ {a_vista:.2f}\n2. Em 6 parcelas. Total: R$ {em_6_parcelas:.2f}\n   6 x R$ {parcelas_6:.2f}\n3. Em 10 parcelas. Total: R$ {valor_da_passagem:.2f}\n   10 x R$ {parcelas_10:.2f}")
