area = float(input())
metro = float(input())
pagamento = input()
calculo = area * metro
desconto_a_vista = (calculo * 20) / 100
conta1 = calculo - desconto_a_vista
desconto_2x = (calculo * 10) / 100
conta2 = calculo - desconto_2x
conta2_2 = conta2 / 2
desconto_3x = (calculo * 5) / 100
conta3 = calculo - desconto_3x
conta3_3 = conta3 / 3
if pagamento == "vista":
    print(f"Total: R$ {conta1:.2f}")
elif pagamento == "2x":
    print(f"Total: R$ {conta2:.2f}. Parcelas: R$ {conta2_2:.2f}")
elif pagamento == "3x":
    print(f"Total: R$ {conta3:.2f}. Parcelas: R$ {conta3_3:.2f}")

