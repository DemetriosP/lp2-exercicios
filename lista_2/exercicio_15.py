lado_1 = int(input("Informe o primeiro lado do tringaulo: "))
lado_2 = int(input("Informe o segundo lado do tringaulo: "))
lado_3 = int(input("Informe o terceiro lado do tringaulo: "))

if lado_2 - lado_3 < lado_1 < lado_2 + lado_3 and \
        lado_1 - lado_3 < lado_2 < lado_1 + lado_3 and \
        lado_1 - lado_2 < lado_3 < lado_1 + lado_2:
    if lado_1 == lado_2 == lado_3:
        print("Os lados formam um triangulo equilátero")
    elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
        print("O lados formam um triangulo isósceles")
    else:
        print("Os lados formam um triangulo escaleno")
else:
    print("Os lados não podem formar um triangulo")
