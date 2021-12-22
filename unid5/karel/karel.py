vertical = 0
horinzontal = 0

while True:
    entrada = input().split()

    if entrada[1] == '0':
        print("Fim de jogo")
        break

    if entrada[0] == 'C':
        vertical += int(entrada[1])
    if entrada[0] == 'B':
        vertical -= int(entrada[1])
    if entrada[0] == 'D':
        horinzontal += int(entrada[1])
    if entrada[0] == 'E':
        horinzontal -= int(entrada[1])

    if abs(horinzontal*2) == abs(vertical) and vertical != 0:
        print(f"Parabéns, conquista do portal ({horinzontal}, {vertical})")
        break
