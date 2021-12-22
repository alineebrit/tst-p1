conta = input()
soma = int(conta[0]) + int(conta[1]) + int(conta[2]) + int(conta[3]) + int(conta[4])
resto = soma % 11
print(f"{conta}-{resto:0>2}")
