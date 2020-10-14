def limpiaLista(lista):
    """Recibe una lista con \n y
    la regresa limpia de \n"""
    for pos in range(len(lista)):
        lista[pos] = lista[pos].rstrip()
        
    return lista

def initMatrizArchivo(nomArch):
    with open(nomArch + ".txt","r") as archivo:
        datos = archivo.readlines()
        
    datos = limpiaLista(datos)
    #print(datos)
    numRen = int(datos[0][0])
    numCol = int(datos[0][2])
    #print(numRen,numCol)
    #print(len(datos))
    if (numRen + 2) != len(datos):
        print("Error. Cantidad de renglones en el archivo mal.")
        return []
    else:
        renglones = datos[1:len(datos)-1]
        #print(renglones)
        for pos in range(len(renglones)):
            renglones[pos] = renglones[pos].split(",")
        #print(renglones)
        for ren in range(numRen):
            for col in range(numCol):
                renglones[ren][col] = int(renglones[ren][col])
        #print(renglones)
        return renglones
