codigo = int(input())

if codigo == 1:
    salario = 25000
    print(f"Deverá receber em dezembro R$ {salario:.2f}.")
elif codigo == 2:
    salario = 15000
    print(f"Deverá receber em dezembro R$ {salario:.2f}.")
elif codigo == 3:
    dias_trabalhados = int(input())
    if dias_trabalhados != 0:
        gratificacao = (235-dias_trabalhados)*2.0
        salario_t = 8000 + gratificacao
        print(f"Valor da gratificação R$ {gratificacao:.2f}.")
        print(f"Deverá receber em dezembro R$ {salario_t:.2f}.")
    else:
        gratificacao = 500
        salario = 8000
        salario_t = salario + gratificacao
        print(f"Valor da gratificação R$ {gratificacao:.2f}.")
        print(f"Deverá receber em dezembro R$ {salario_t:.2f}.")
elif codigo == 4:
    dias_trabalhados = int(input())
    if dias_trabalhados != 0:
        gratificacao = (235-dias_trabalhados)*1.0
        salario_t = 5000 + gratificacao
        print(f"Valor da gratificação R$ {gratificacao:.2f}.")
        print(f"Deverá receber em dezembro R$ {salario_t:.2f}.")
    else:
        gratificacao = 300
        salario = 5000
        salario_t = salario + gratificacao
        print(f"Valor da gratificação R$ {gratificacao:.2f}.")
        print(f"Deverá receber em dezembro R$ {salario_t:.2f}.")
elif codigo == 5:
    dias_trabalhados = int(input())
    if dias_trabalhados != 0:
        gratificacao= (235-dias_trabalhados)*0.7
        salario_t = 2800 + gratificacao
        print(f"Valor da gratificação R$ {gratificacao:.2f}.")
        print(f"Deverá receber em dezembro R$ {salario_t:.2f}.")
    else:
        gratificacao = 200
        salario = 2800
        salario_t = salario + gratificacao
        print(f"Valor da gratificação R$ {gratificacao:.2f}.")
        print(f"Deverá receber em dezembro R$ {salario_t:.2f}.")
