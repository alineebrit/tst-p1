quantidade = int(input())
pagina = quantidade // 400
resto = quantidade % 400
porcentagem = 100 * resto / quantidade
print(f"Serão necessárias {pagina:.0f} página(s) para visualizar os tweets.")
print(f"{porcentagem:.1f}% dos tweets serão perdidos.")
