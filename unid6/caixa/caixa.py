def caixa_registradora(vendas,meta):
    total = 0
    comissoes = 0
    situacao = None
    for e in vendas:
        if e < 1000:
            total += e
            comissoes += (5/100) * e
        elif e >= 1000 and e < 5000:
            total += e
            comissoes += (10/100) * e
        elif  e >= 5000:
            total += e
            comissoes += (15/100) * e
    if total >= meta:
        situacao = "Lucro"
    else:
        situacao = "Prejuizo"

    return [total ,comissoes, situacao]

assert caixa_registradora([1000.0, 2000.0, 5000.0, 2500.0, 950.0], 2000.0) == [11450.0, 1347.5, 'Lucro']
