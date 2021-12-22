nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
faltas = int(input())

porcentagem_faltas = (faltas * 100) / 30
porcentagem_presenca = 100 - porcentagem_faltas
media = (nota1 + nota2 + nota3) / 3
if porcentagem_presenca >= 75 and media >= 7:
    print("aprovado por media")
elif porcentagem_presenca < 75:
    print("reprovado por faltas")
elif porcentagem_presenca >= 75 and media < 4:
    print("reprovado por nota")
elif porcentagem_presenca >= 75 and media >= 4 and media <7:
    print("prova final")



