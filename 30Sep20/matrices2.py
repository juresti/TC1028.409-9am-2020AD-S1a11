def crearMatriz(numRen,numCol,valor):
    matriz = []
    for ren in range(numRen):
        renglon = []
        for col in range(numCol):
            renglon.append(valor)
        matriz.append(renglon)
    return matriz

def tamanoMatriz(matriz):
    if (matriz == []):
        return 0,0 #(0,0)
    else:
        numRen = len(matriz)
        numCol = len(matriz[0])
        for renglon in matriz:
            if (len(renglon) != numCol):
                print("Matriz mal formada")
                return -1,-1 #Valor de error en matriz
        return numRen,numCol

def mismoTamano(matriz1,matriz2):
    numRen1, numCol1 = tamanoMatriz(matriz1)
    numRen2, numCol2 = tamanoMatriz(matriz2)
    if (numRen1 == -1) or (numRen2 == -1): #caso error
        print("Error: Matrices mal formadas")
        return -1 #Valor
    else:
        if(numRen1 == numRen2):
            if(numCol1 == numCol2):
                return True
            else:
                print("Numero de columnas diferente")
                return False
        else:
            print("Numero de renglones diferente")
            return False
        
def restaMatrices(mat1,mat2):
    if mismoTamano(mat1,mat2):
        numRen,numCol = tamanoMatriz(mat1)
        resta = crearMatriz(numRen,numCol,0)
        for ren in range(numRen):
            for col in range(numCol):
                resta[ren][col] = mat1[ren][col] - mat2[ren][col]
        return resta
    else:
        print("Matrices no son del mismo tamaño")
        return []