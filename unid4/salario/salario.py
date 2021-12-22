ano = int(input())
ano_final = int(input())
contador_acima = 0
contador_abaixo = 0
ano_resultante = ano_final - ano + 1
salario_acima = 0
salario_abaixo = 0
for a in range(ano_resultante):
    salario = float(input())
    if salario > 100:
        salario_acima += salario
        contador_acima += 1
    else:
        contador_abaixo += 1
        salario_abaixo += salario
percentual_abaixo = (100 * contador_abaixo) / ano_resultante
print(f"{contador_abaixo} ano(s) abaixo ({round(percentual_abaixo)}% dos anos)")
if contador_abaixo > 0:
    media_abaixo = (salario_abaixo / contador_abaixo)
    print(f"média dos anos abaixo: U$ {media_abaixo:.2f}")

percentual_acima = (100 * contador_acima) / ano_resultante
print(f"{contador_acima} ano(s) acima ({round(percentual_acima)}% dos anos)")
if contador_acima > 0:
    media_acima = (salario_acima / contador_acima)
    print(f"média dos anos acima: U$ {media_acima:.2f}")



