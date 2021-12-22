capacidade = float(input("Capacidade de revestimento? "))
print(f"\n== Dados do vão a revestir ==")
comprimento = float(input("Comprimento? "))
largura = float(input("Largura? "))
altura = float(input("Altura? "))

at = 2 * (( largura * comprimento) + (comprimento * altura) + (largura * altura))
ab = largura * comprimento
revestir = at - ab
caixas = revestir / capacidade


print(f"\n== Resultados ==")
print(f"Área total a revestir: {revestir:.1f} m2")
print(f"Número de caixas: {caixas:.0f}")
