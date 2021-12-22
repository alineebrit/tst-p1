nota1_1 = float(input())
nota1_2 = float(input())
nota1_3 = float(input())
idade1 = int(input())

nota2_1 = float(input())
nota2_2 = float(input())
nota2_3 = float(input())
idade2 = int(input())

media1 = ((nota1_1 * 0.3) + (nota1_2 * 0.4) + (nota1_3 * 0.3)) / 1
media2 = ((nota2_1 * 0.3) + (nota2_2 * 0.4) + (nota2_3 * 0.3)) / 1
if media1 > media2:
    print(f"O primeiro candidato foi aprovado com média {media1:.1f}.")
elif media2 > media1:
    print(f"O segundo candidato foi aprovado com média {media2:.1f}.")
elif media1 == media2 and idade1 > idade2:
    print(f"O primeiro candidato foi aprovado com média {media1:.1f}.")
elif media1 == media2 and idade2 > idade1:
    print(f"O segundo candidato foi aprovado com média {media2:.1f}.")
elif media1 == media2 and idade1 == idade2:
    print("Empate.")
