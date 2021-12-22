produzido = float(input())
atacado = float(input())
varejo = float(input())
divisao = produzido // atacado
resto = produzido % atacado
div_var = resto / varejo
print(f"Clientes no atacado = {divisao:.0f}kg cada.\nClientes no varejo = {div_var:.2f}kg cada.")
