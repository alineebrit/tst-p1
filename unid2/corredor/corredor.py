distancia_percorrida = float(input())
tempo_em_min = int(input())
tempo_em_seg = int(input())

tempo_total = ((tempo_em_min * 60) + tempo_em_seg)
pace = int(tempo_total  / distancia_percorrida)
resto = pace % 60
divisor = pace // 60

print(f"O pace foi de {divisor}min{resto}s.")
