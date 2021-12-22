a = input()
b = input()
c = input()
if a[0] < b[0] and a[0] < c[0]:
    print(f"{a} (1)")
elif b[0] < a[0] and b[0] < c[0]:
    print(f"{b} (1)")
elif c[0] < b[0] and c[0] < a[0]:
    print(f"{c} (1)")
elif a[0] == b[0] or a[0] == c[0]:
    print(f"{a} (2)")
elif b[0] == c[0]:
    print(f"{b} (2)")
