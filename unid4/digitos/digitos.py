com = 0
N = int(input())
for i in range(N):
    senha =  input()
    for j in range(len(senha)-1):
        if senha[j] == senha[j+1]:
            com += 1
            break
sem =  N - com

print(f"com: {com}")
print(f"sem: {sem}")
