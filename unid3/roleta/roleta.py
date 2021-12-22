angulo = float(input())
angulo = angulo % 360
if angulo > 0 and angulo < 90: 
    print("Quadrante 1")
elif angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360:
    print("Sobre eixos")
elif angulo < 180:
    print("Quadrante 2")
elif angulo < 270:
    print("Quadrante 3")
elif angulo < 360:
    print("Quadrante 4")

