n1 = int(input())
n2 = int(input())
n3 = int(input())

soma = n1 + n2 + n3
if soma % 3 == 0 and soma % 5 == 0:
    print("plifplof")
elif soma % 3 == 0:
    print("plif")
elif soma % 5 == 0:
    print("plof")
else:
    print(f"{soma}")
