n = int(input())
palavras = []
for i in range(n):
    palavra = input()
    palavras.append(palavra)
print("---")
antes = 0
depois = 0
referencia = input()
for palavra in palavras:
    if (palavra < referencia):
        antes += 1
    elif (palavra > referencia):
        depois += 1
print(f"{antes} antes")
print(f"{depois} depois")


