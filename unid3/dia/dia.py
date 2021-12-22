dia, venda = input().split(" ")
movimento = ""

vendas = int(venda)

if dia == "sábado" or dia == "domingo":
    if vendas>=20:
        movimento = "normal"
    else:
        movimento = "fraco"
else:
    if vendas>30:
        movimento = "atípico"
    elif vendas >= 20:
        movimento = "normal"
    else:
        movimento = "fraco"

print(f"{movimento}")
