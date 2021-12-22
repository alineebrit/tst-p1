limite = float(input())

while True:
  entrada = input()

  if entrada == 'fim':
    break

  sequencia = entrada.split()

  soma = 0
  for i in range(len(sequencia)):
    soma += float(sequencia[i])

  media = soma / len(sequencia)

  if media < (limite / 2):
    break
  
  if media > limite:
    mensagem = ''
    for i in range(len(sequencia)):
      mensagem += str(float(sequencia[i])) + ' '
    
    print(mensagem.strip())
