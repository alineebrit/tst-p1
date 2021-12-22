convidados = float(input())
op1_inteira = 32 // convidados
op1_resto  = 32 % convidados
op2 = 32 / convidados
print(f"Opção 1: {op1_inteira:.0f} fatias cada, {op1_resto:.0f} de resto")
print(f"Opção 2: {op2:.2f} fatias cada")

