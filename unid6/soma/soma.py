def soma_diminui_vizinhos(valores):
  if not valores: return 0
  
  somatorio = valores[0]
  for i in range(1, len(valores)):
    if i % 2 == 0:
      somatorio += valores[i] * -1
    else:
      somatorio += valores[i]
  
  return somatorio
