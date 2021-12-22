mensagens = []
valor_limite = int(input())

while True:
  entrada = input()

  if entrada == '-':
    break

  sequencia = entrada.split()

  soma = 0
  for i in range(len(sequencia)):
    soma += int(sequencia[i])

  mensagem = ""
  for i in range(len(sequencia)):
    mensagem += sequencia[i]

    if i != len(sequencia) - 1:
      mensagem += " + "

  mensagem += " = " + str(soma)

  if soma >= valor_limite:
    mensagens.append(mensagem)

  if soma > (valor_limite * 5):
    break

for i in range(len(mensagens)):
  print(mensagens[i])
