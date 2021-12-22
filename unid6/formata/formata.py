def separa_frase(frase):
    str_vazia = ''
    separada = []
    for letra in frase:
        if letra != " ": str_vazia += letra
        else:
            separada.append(str_vazia)
            str_vazia = ''
    if str_vazia: separada.append(str_vazia)
    return separada

def ultimo_nome(autores):
    ultimosnomes = separa_frase(autores)
    
    return ultimosnomes[len(ultimosnomes) - 1]

def fmt_citacao(autores):
    lista_final = []
    for nome in autores:
        lista_final.append(f'{ultimo_nome(nome)}, {nome[0]}.')
    return lista_final
