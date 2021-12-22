capacidade = float(input("capacidade? "))
percentual = float(input("percentual hoje? "))
consumo_diario = float(input("gasto diário? "))
volume = (capacidade * percentual) /100 
dias_restantes = volume // consumo_diario
print(f"volume: {volume:.2f}\ndias restantes: {dias_restantes:.0f}") 

