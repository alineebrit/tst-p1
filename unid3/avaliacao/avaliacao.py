n_semestres = int(input())
ensino = int(input())
p_intelectual = int(input())
orientacao = int(input())
administrativas = int(input())

soma = ensino + p_intelectual + orientacao + administrativas
media = soma / 4
if n_semestres < 4:
    print("Promoção indeferida. Número de semestres insuficiente.")
elif soma < 320 or ensino < 320 or p_intelectual < 100 or orientacao < 20:
    print("Promoção indeferida. Pontuação mínima não alcançada.")
elif media < 140:
    print("Promoção indeferida. Média insuficiente.")
elif media > 140 and ensino == 320 or ensino > 320 and p_intelectual == 100 or p_intelectual > 100 and orientacao == 20 or orientacao > 20:
    print("Promoção deferida. Parabéns!")

