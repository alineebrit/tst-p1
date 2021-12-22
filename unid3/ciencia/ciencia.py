enem = float(input())
creditos = float(input())
porcentagem = (creditos * 100) / 416

if enem >= 600:
    if 20 <= porcentagem and porcentagem <= 90:
        print("Todas as condições satisfeitas.")
    else:
        print("Condição CRÉDITOS não satisfeita.")
else:
    if porcentagem < 20 or 90 < porcentagem:
        print("Nenhuma condição satisfeita.")
    else:
        print("Condição ENEM não satisfeita.")
