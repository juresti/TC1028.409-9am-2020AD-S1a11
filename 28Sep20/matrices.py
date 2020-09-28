def crearMatriz(numRen,numCol,valor):
    matriz = []
    for ren in range(numRen):
        renglon = []
        for col in range(numCol):
            renglon.append(valor)
        print(f"Renglon creado = {renglon}")
        matriz.append(renglon)
        print(f"Matriz hasta el momento = {matriz}")
    return matriz
        
def pideMatriz(numRen,numCol):
    """Pide los valores de la matriz al usuario
    Recibe el numero de renglones y de columnas"""
    matriz = []
    for ren in range(numRen):
        renglon = []
        for col in range(numCol):
            valor = int(input(f"Dime el valor de la posicion ({ren+1},{col+1}): "))
            renglon.append(valor)
        print(f"Renglon creado = {renglon}")
        matriz.append(renglon)
        print(f"Matriz hasta el momento = {matriz}")
    return matriz

def imprimirMatriz(matriz):
    matStr = ""
    for ren in range(len(matriz)):
        renglon = ""
        for col in range(len(matriz[0])):
            renglon += str(matriz[ren][col]) + " "
            #print(f"Renglon creado = {renglon}")
        matStr += renglon + "\n"
        #print(f"Matriz hasta el momento = {matStr}")
    print(matStr)
    return matStr