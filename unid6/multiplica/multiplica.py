def multiplica_lista(n,lista):
  nova = []
  if n == 0:

    return nova
  else:
    nova = (n * lista)

  return nova

l = ['joao', 'pedro']
assert multiplica_lista(2,l) == ['joao', 'pedro', 'joao', 'pedro']
