palavra = input()
for i in range(len(palavra)):
    if (palavra[i] in "AaEeIiOoUu"):
        print(f"<{palavra[i]}> sim")
    else:
        print(f"<{palavra[i]}> nao")


