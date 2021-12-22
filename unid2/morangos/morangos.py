morangos_colhidos = float(input())
caixa = morangos_colhidos // 400
resto = morangos_colhidos % 400 
porcentagem = (resto * 100) / morangos_colhidos
print(f"Serão necessárias {caixa:.0f} caixa(s) para embalar os morangos.\n{porcentagem:.1f}% dos morangos serão perdidos.")

