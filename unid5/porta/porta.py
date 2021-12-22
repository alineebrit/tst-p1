lista = []

saida = []

while True:

  entrada = input() 

  if entrada == "S":
    break

  if entrada[0] == "R":
    
    lista.append(entrada)

  contador = 0

  if entrada[0] == "P": # P A

    for elemento in lista:

      if elemento[2] == entrada[2]:

        contador += 1

    saida.append(contador)
    contador = 0


for e in saida:
  print(e)
