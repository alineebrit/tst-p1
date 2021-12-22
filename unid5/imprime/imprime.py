numero_alvo = int(input())
sequencia = input()
contador_sequencia = 1

while (sequencia != "fim"):
  contador_maiores = 0
  lista = sequencia.split(" ")

  for elemento in lista:
    if( int(elemento) > numero_alvo ):
      contador_maiores += 1
  
  if(contador_maiores > len(lista)/2):
    print("sequencia {}: {}".format(contador_sequencia, sequencia))

  sequencia = input()
  contador_sequencia += 1
