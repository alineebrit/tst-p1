custo_de_entrada = float(input())
despesas_indiretas = float(input())
lucro_desejado = float(input())
impostos = float(input())
comissoes = float(input())
descontos = float(input())
encargos = float(input())
percentual = 100 - (impostos + comissoes + descontos + encargos) 
preco_de_venda = ((custo_de_entrada) + (custo_de_entrada * ((despesas_indiretas + lucro_desejado) / 100))) * 100 
resultado = preco_de_venda / percentual
print(f"Preço de venda é R$ {resultado:.2f} (R$ {(resultado // 1):.2f} + R$ {(resultado % 1):.2f})")
