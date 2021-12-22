valor_do_salario = float(input())
valor_do_empregador = valor_do_salario * 0.12

if valor_do_salario <= 1317.07:
	valor_do_empregado = valor_do_salario * 0.08
	print(f"O valor da contribuição do INSS a ser pago pelo empregador é de R$ {valor_do_empregador:.2f}")
	print(f"O valor da contribuição do INSS a ser pago pelo empregado é de R$ {valor_do_empregado:.2f}")

elif valor_do_empregador >= 2195.11:
	valor_do_empregado = valor_do_salario * 0.09
	print(f"O valor da contribuição do INSS a ser pago pelo empregador é de R$ {valor_do_empregador:.2f}")
	print(f"O valor da contribuição do INSS a ser pago pelo empregado é de R$ {valor_do_empregado:.2f}")

else :
	valor_do_empregado = valor_do_salario * 0.11
	print(f"O valor da contribuição do INSS a ser pago pelo empregador é de R$ {valor_do_empregador:.2f}")
	print(f"O valor da contribuição do INSS a ser pago pelo empregado é de R$ {valor_do_empregado:.2f}")
