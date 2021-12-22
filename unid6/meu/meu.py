def meu_join(delimitador, sequencia):
  sequencia_final = ''
  for i in range(len(sequencia)):
    if i < (len(sequencia) - 1):
      sequencia_final += f'{sequencia[i]}{delimitador}'
    else:
      sequencia_final += sequencia[i]
  
  return sequencia_final
