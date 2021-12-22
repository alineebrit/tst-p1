dna1 = input()
dna2 = input()
dna3 = input()

tamanho_dna1 = len(dna1)
tamanho_dna2 = len(dna2)
tamanho_dna3 = len(dna3)
menor = ''
frase = ''

if tamanho_dna1 <= tamanho_dna2 and tamanho_dna1 <= tamanho_dna3:
    menor = tamanho_dna1
    frase = dna1
elif tamanho_dna2 < tamanho_dna1 and tamanho_dna2 < tamanho_dna3:
    menor = tamanho_dna2
    frase = dna2
elif tamanho_dna3 < tamanho_dna1 and tamanho_dna3 < tamanho_dna2:
    menor = tamanho_dna3
    frase = dna3

print(frase,menor)
