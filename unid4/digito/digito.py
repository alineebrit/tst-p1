conta = input()
soma = 0

for a in (conta):
    soma += int(a)
    digito = soma % 11
if digito == 10:
    print(f"{conta}-X")
else:
    print(f"{conta}-{digito}")
