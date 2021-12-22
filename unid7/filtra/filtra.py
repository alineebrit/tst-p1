def filtra_caixas_indisponiveis(lista_caixas, qtd_itens):
  for i in range(len(lista_caixas) -1, -1, -1):
    if lista_caixas[i] < qtd_itens:
      lista_caixas.pop(i)
