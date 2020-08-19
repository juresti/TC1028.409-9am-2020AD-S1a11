X = int(input("Dime el lado 1: "))
Y = int(input("Dime el lado 2: "))
Z = int(input("Dime el lado 3: "))

if(X > 0) and (Y > 0) and (Z > 0):
    if(X+Y > Z) and (X+Z > Y) and (Y+Z > X):
        if (X == Y == Z):
            print("Triangulo equilatero")
        elif (X != Y != Z):
            print("Triangulo escaleno")
        else:
            print("Triangulo isosceles")
    else:
        print("Las sumas no se cumplen")
else:
    print("Todos los lados deben de ser mayores a cero")