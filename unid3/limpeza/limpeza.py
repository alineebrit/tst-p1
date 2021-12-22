numero = int(input())
if numero == 1:
    tamanho = int(input())
    valor = 80 * tamanho
    print(f"R$ {valor},00")
    if valor > 200 or valor == 200:
        print("Brinde!")
elif numero == 2:
    tamanho = int(input())
    valor= 50 * tamanho
    print(f"R$ {valor},00")
    if valor > 200 or valor == 200:
        print("Brinde!")
elif numero == 3:
    print("R$ 50,00")
