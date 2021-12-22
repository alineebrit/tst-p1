def calculaPeso(sexo, altura):
  frase = ''

  if sexo == 'F' or sexo == 'f':
    conta = (62.1 * altura) - 44.7
    frase = f'Mulher: peso ideal é {conta:.1f}'
  elif sexo == 'M' or  sexo == 'm':
    conta = (72.7 * altura) - 58
    frase = f'Homem: peso ideal é {conta:.1f}'

  return frase

while True:
  entrada = input()

  if entrada == "****": break

  sexo, altura = entrada.split()

  frase = calculaPeso(sexo, float(altura))

  print(frase)
