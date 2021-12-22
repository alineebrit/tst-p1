def meu_split(lista):
    aspas = ''
    splitt = []
    for letra in lista:
        if letra != " ":
            aspas += letra
        else:
            splitt.append(aspas)
            aspas = ''
    if aspas:
        splitt.append(aspas)
    return splitt

def maioridade_penal(nomes, idades):
  nomes = meu_split(nomes)
  idades = meu_split(idades)
  lista = ''
  for i in range(len(idades)):
    if idades[i] >= "18":
      if i < len(idades) - 1:
        lista += f'{nomes[i]} '
      else:
        lista += f'{nomes[i]}'
  return lista
assert maioridade_penal("Jansen Italo Ana","14 21 60") == "Italo Ana"
