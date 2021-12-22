po = float(input("Posição inicial? "))
vo = float(input("Velocidade inicial? "))
td = float(input("Tempo? "))
am = float(input("Aceleração? "))
v = vo+(am*td)
s = po+(vo*td)+((am*(td**2))/2)
vm = (vo+v)/2
print("\nDados da questão")
print("================")
print(f"   Posição inicial: {po:.2f} m")
print(f"Velocidade inicial: {vo:.2f} m/s")
print(f"        Aceleração: {am:.2f} m/s2")
print(f"             Tempo: {td:.2f} s")
print(f"  Velocidade final: {v:.2f} m/s")
print(f"  Velocidade média: {vm:.2f} m/s")
print(f"     Posição final: {s:.2f} m")


