def concatena_simetricos(valores):
    list = []

    if len(valores) % 2 == 0:

        for i in range(len(valores) // 2):

            op = (len(valores) - 1) - i
            if valores[i][0]  <= valores[op][0]:  

                junta = (valores[i] + valores[op])
            else:

                junta = (valores[op] + valores[i])
            list.append(junta)

    else:

        for i in range(int(len(valores) / 2)):

            op = (len(valores) - 1) - i

            if valores[i][0]  <= valores[op][0]:  
                junta = (valores[i] + valores[op])

            else:
                junta = (valores[op] + valores[i])
            list.append(junta)
        list.append(valores[(int(len(valores) / 2))])
    return list
