nome = input()
horas_extra = float(input())
valor_salario = float(input())
valor_extra = float(input())
salario_extra = horas_extra * valor_extra
salario_bruto = (4 * valor_salario) + salario_extra
desconto_inss = (12 / 100) * salario_bruto
desconto_ipr = (20 / 100) * salario_bruto
sl = (salario_bruto - desconto_inss) - desconto_ipr
print(f"O Salário Bruto de Antonio é de R$ {salario_bruto:.2f}")
print(f"O Salário Líquido de Antonio é de R$ {sl:.2f}")
