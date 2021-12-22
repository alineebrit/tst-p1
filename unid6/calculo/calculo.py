def calcula_seguro(valor, respostas):
    pontos = 0
    resultado = []
    for i in range(len(respostas)):
        if i == 0:
            if respostas[i] <= 21: 
                pontos += 20
            elif respostas[i] >= 22 and respostas[0] <= 30: 
                pontos += 15
            elif respostas[i] >= 31 and respostas[0] <= 40: 
                pontos += 12
            elif respostas[i] >= 41 and respostas[0] <= 60: 
                pontos += 10
            elif respostas[i] > 60: 
                pontos += 20
        if i == 1:
            if respostas[i] == True: 
                pontos += 10
            elif respostas[i] == False:
                pontos += 20
        if i == 2:
            if respostas[i] == True: 
                pontos += 20
            elif respostas[i] == False: 
                pontos += 10
        if i == 3:
            if respostas[i] == True: 
                pontos += 20
            elif respostas[i] == False: 
                pontos += 10
        if i == 4:
            if respostas[i] == True: 
                pontos += 20
            elif respostas[i] == False: 
                pontos += 10
        if i == 5:
            if respostas[i] == True:
                pontos += 10
            elif respostas[i] == False: 
                pontos += 20
        if i == 6:
            if respostas[i] == 'Trabalho': 
                pontos += 10
            elif respostas[i] == 'Lazer':
                pontos += 20
            elif respostas[i] == 'Misto': 
                pontos += 20
    if pontos <= 80:
        perfil = 'Risco Baixo'
        valorseguro = valor * 0.1
    elif pontos > 80 and pontos <= 100:
        perfil = 'Risco Medio'
        valorseguro = valor * 0.2
    elif pontos > 100:
        perfil = 'Risco Alto'
        valorseguro = valor * 0.3
    resultado.append(pontos)
    resultado.append(perfil)
    resultado.append(valorseguro)

    return resultado
