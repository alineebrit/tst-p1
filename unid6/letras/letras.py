def letras_alternadas(palavras):
  if len(palavras) % 2 == 0:
    aspas = ''
    ind = 0
    for i in range(len(palavras)//2):
      aspas += palavras[ind]
      ind += 2
  else:
    aspas = ''
    ind = 0
    for i in range((len(palavras)//2) + 1):
      aspas += palavras[ind]
      ind += 2
  return aspas

assert letras_alternadas("casa") == 'cs'
assert letras_alternadas("exemplo") == "eepo"
