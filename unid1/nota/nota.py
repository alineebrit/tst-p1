valor_t = float(input())
data = input()
quantidade_produtos = int(input())
media = valor_t / quantidade_produtos
print(f"Data: {data}")
print(f"O valor total da compra foi de R$ {valor_t:.2f}. A média do preço dos produtos é de {media:.1f}.")
