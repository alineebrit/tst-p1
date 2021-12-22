dia1 = int(input())
dia2 = int(input())
dia3 = int(input())
dia4 = int(input())
dia5 = int(input())
tempo_total = dia1 + dia2 + dia3 + dia4 + dia5
media_total = tempo_total/5 
porcentagem = (tempo_total * 100) / 7200
tempo_gasto = tempo_total//50

print(f"Você perdeu {tempo_total} min na semana (média de {media_total:.1f} min por dia).")
print(f"Isso significa {porcentagem:.2f}% da sua semana produtiva.")
print(f"Daria para assistir {tempo_gasto:.0f} episódio(s) de House.")
