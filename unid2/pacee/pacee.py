distancia_percorrida = float(input())
tempo_em_min = int(input())
tempo_em_seg = int(input())

tempo_t = ((tempo_em_min * 60) + tempo_em_seg)
pace = tempo_t  // distancia_percorrida
resto = round(pace % 60)
divisor = pace // 60
print(f"O pace foi de {divisor:.0f}min{resto}s.")
