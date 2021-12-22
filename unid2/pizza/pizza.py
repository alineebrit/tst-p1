numero_de_amigos = int(input())
quantidade_de_pizza = int(input())
preco = float(input())

fatias = quantidade_de_pizza * 8
comer = fatias // numero_de_amigos
resto = fatias % numero_de_amigos
valor = quantidade_de_pizza * preco

print(f"{comer} fatia(s) para cada um e sobra(m) {resto} fatia(s)")
print(f"Valor total: R$ {valor:.2f}")
