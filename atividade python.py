ladoA = int(input("Digite o lado A = "))
ladoB = int(input("Digite o lado B = "))
ladoC = int(input("Digite o lado C = "))
if (ladoA < (ladoB + ladoC)) and (ladoB < (ladoA + ladoC)) and (ladoC <(ladoA + ladoB)):
    if ((ladoA == ladoB) and (ladoB == ladoC)):
        print("Triangulo Equilatero!")
    elif (ladoA == ladoB) or (ladoB == ladoC) or (ladoA == ladoC):
        print("Triangulo Isosceles!")
    else:
        print("Triangulo Escaleno!")
else:
    print("Lados não formam um triangulo!")