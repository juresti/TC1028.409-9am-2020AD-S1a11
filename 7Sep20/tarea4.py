def linea(ancho):
    strLin = ""
    for cont in range(ancho):
        strLin += "*"
    return strLin

def rectSolido(ancho,alto):
    rect = ""
    for cont in range(alto):
        rect += linea(ancho) + "\n"
    return rect

def lineaEsp(ancho):
    strLin = "*"
    for cont in range(ancho - 2):
        strLin += " "
    strLin += "*"
    return strLin
    
def rectEsp(ancho,alto):
    rect = linea(ancho) + "\n"
    for cont in range(alto - 2):
        rect += lineaEsp(ancho) + "\n"
    rect += linea(ancho) + "\n"
    return rect

def variosRectEsp(ancho,alto,num):
    salida = ""
    for cont in range(num):
        salida += rectEsp(ancho,alto) + "\n"
    return salida

def letraU(ancho,alto):
    strLet = ""
    for cont in range(alto - 1):
        strLet += lineaEsp(ancho) + "\n"
    strLet += linea(ancho)
    return strLet

def rectJuntos(ancho,alto,num):
    rect = linea(ancho) + "\n"
    for cont in range(num):
        rect += letraU(ancho,alto - 1) + "\n"
    return rect
        

def main():
    #Ejercicio 1
    print("Ejercicio 1 **********\n Rectangulo solido")
    alt = int(input("Dime la altura: "))
    ancho = int(input("Dime el ancho: "))
    print(rectSolido(ancho,alt))
    
    #Ejercicio 2
    print("\nEjercicio 2 *****\n Rectangulo espacios")
    alt = int(input("Dime la altura: "))
    ancho = int(input("Dime el ancho: "))
    print(rectEsp(ancho,alt))
    
    #Ejercicio 3
    print("\nEjercicio 3 *****\n Varios Rectangulos espacios")
    alt = int(input("Dime la altura: "))
    ancho = int(input("Dime el ancho: "))
    numero = int(input("Numero de rectangulos: "))
    print(variosRectEsp(ancho,alt,numero))
    