N = int(input())
contador_n = 0
Soma = 0
for i in range(N):
    duplas = input().split(' ')
    if duplas[0] != duplas[1]:
        contador_n += 1
        if int(duplas[0]) <  int(duplas[1]):
            Soma += int(duplas[1])
        else:
            Soma += int(duplas[0])


if contador_n == 0:
    print('Não é possível calcular a média.')
else:
    print(f'{(Soma / contador_n):.2f}')



