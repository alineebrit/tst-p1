total = int(input())
rafael = int(input())
gabriela = int(input())
mateus = int(input())
larissa = int(input())

p_rafael = (rafael * 100) / total
p_gabriela = (gabriela * 100) / total
p_mateus = (mateus * 100) / total
p_larissa = (larissa * 100) / total
p_total = 100 - (p_rafael + p_gabriela + p_mateus + p_larissa)
n_total = total - (rafael + gabriela + mateus + larissa) 
media = (rafael + gabriela + mateus + larissa) / 4

print(f"Em média, os 4 amigos venderam {media:.2f} bilhete(s)")
print(f"{n_total} bilhete(s) sem vender ({p_total:.2f}%)")
print(f"Rafael vendeu {rafael} bilhete(s) ({p_rafael:.2f}%)")
print(f"Gabriela vendeu {gabriela} bilhete(s) ({p_gabriela:.2f}%)")
print(f"Mateus vendeu {mateus} bilhete(s) ({p_mateus:.2f}%)")
print(f"Larissa vendeu {larissa} bilhete(s) ({p_larissa:.2f}%)")

