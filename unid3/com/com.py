n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

if n1 == n2 or n1 == n3 or n1 == n4 or n1 == n5:
    print(f"com duplicados")

elif n2 == n3 or n2 == n4 or n2 == n5:
    print(f"com duplicados")

elif n3 == n4 or n3 == n5:
    print(f"com duplicados")

elif n4 == n5:
    print(f"com duplicados")

else:
    print(f"sem duplicados")
