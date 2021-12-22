penalizacao = 0
soma_notas = 0
quantidade_notas = 0
media_notas = 0
maior_nota = 0
segunda_maior_nota = 0
print('Mastery Learning')
print('Cálculo da nota na unidade')
print()

while True:
    nota = float(input('Nota? '))
    quantidade_notas += 1
    soma_notas += nota
    if quantidade_notas == 1:
        maior_nota = nota
    elif quantidade_notas == 2:
        segunda_maior_nota = nota
    else:
        if nota >= maior_nota and nota > segunda_maior_nota:
            maior_nota = nota
        elif nota < maior_nota and nota >= segunda_maior_nota:
            segunda_maior_nota = nota
    if quantidade_notas >= 2:
        media_notas = ((maior_nota + segunda_maior_nota) / 2)
        if quantidade_notas >= 3:
            penalizacao += 0.5
        if float(f'{media_notas:.1f}') >= 6.5:
            validacao = 'aprovado'
        else:
            validacao = 'cursando'


        print(f'Média: {media_notas:.1f} ({validacao})')
        print(f'Penalização: {float(penalizacao)}')
        print()
    if media_notas >= 6.5:
        break
media_final = media_notas - penalizacao
print('===')
print(f'Notas válidas: {maior_nota} e {segunda_maior_nota}')
print(f'Média parcial na unidade: {media_notas:.1f}')
print(f'Penalizações: {float(penalizacao)}')
print(f'Média final na unidade: {media_final:.1f}')

