distancia = float(input())
minutos = int(input())
segundos = int(input())
minutos += (segundos / 60)

pace = minutos / distancia
print(f'O pace foi de {int(pace // 1)}min{int((pace % 1) * 60)}s.')
