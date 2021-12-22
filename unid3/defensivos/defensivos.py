produto = str(input()).strip()
area = int(input()) 

import math 

if produto == 'Fungicida':
     x  = math.ceil(area /  50)
     preco = (x  * 320 ) # Medir o preço
     print(f'{x:.0f} Fungicida(s). {preco:.2f} reais.')


elif produto == 'Herbicida': 
     litros  =  area * 0.3
     quantidade = math.ceil(litros / 1)
     preco = quantidade * 100
     print(f'{quantidade:.0f} Herbicida(s). {preco:.2f} reais.') 

elif produto == 'Inseticida': 
     litros = area * 2.5
     quantidade1 = math.ceil (litros/30) 
     preco1 = quantidade1 * 400
     print(f'{quantidade1:.0f} Inseticida(s). {preco1:.2f} reais.')
