numero = int(input())

entrada = numero

divisor = '1'

contador = 0

unid = ''

while int(numero) > 0 or int(numero) < 0:
    numero = numero / 10
    contador += 1


while True:
    unid = (entrada // int(divisor)) % 10

    divisor += '0'

    contador -= 1

    print(unid)
    if contador == 0:
        break
    if numero == 0:
        break
    
