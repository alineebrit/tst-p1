login1 = input()
tamanho1 = float(input())

login2 = input()
tamanho2 = float(input())

login3 = input()
tamanho3 = float(input())

conta1 = (tamanho1 / 1024) / 1024 
conta2 = (tamanho2 / 1024) / 1024
conta3 = (tamanho3 / 1024) / 1024
total = conta1 + conta2 + conta3
media = total / 3

print("SPLab - Espaço utilizado pelos usuários")
print("---------------------------------------------")
print("Nr., Usuário, Espaço Utilizado\n")
print(f"1, {login1}, {conta1:.2f} MB")
print(f"2, {login2}, {conta2:.2f} MB")
print(f"3, {login3}, {conta3:.2f} MB\n")
print(f"Espaço total ocupado: {total:.2f} MB")
print(f"Espaço médio ocupado: {media:.2f} MB")
