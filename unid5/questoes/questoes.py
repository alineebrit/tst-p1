colaboracoes = []
total = 0
cont_questoes = 0

while True:

    colaborador = input()

    if colaborador == '**': break
    cont_questoes = 0
    while True:
        questoes = input()

        if questoes == '*': break

        cont_questoes += int(questoes)

    total += cont_questoes
    colaboracoes.append([colaborador, cont_questoes])

print("Relatório de novas questões:\n")

for colaboracao in colaboracoes:
    print(f"{colaboracao[0]}: {colaboracao[1]}")
    
print("---")
print(f"Total de novas questões: {total}")
