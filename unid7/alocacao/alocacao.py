def alocacao_aulas(alunos):
    turma1 = []
    turma2 = []
    turma3 = []
    for aluno in alunos:
        if aluno[1] <= 3:
            turma1.append(aluno[0])
        elif aluno[1] > 3 and aluno[1] <= 6:
            turma2.append(aluno[0])
        else:
            turma3.append(aluno[0])

    return [turma1, turma2, turma3]
