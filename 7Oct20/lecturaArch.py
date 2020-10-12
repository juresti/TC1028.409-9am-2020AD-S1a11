def leeArchivo(nomArch):
    with open(nomArch + ".txt","r") as archivo:
        lista = archivo.readlines()
        #print(lista)
        
    for pos in range(len(lista)):#limpia \n
        #print(pos)
        #print(lista[pos])
        lista[pos] = lista[pos].rstrip()
        
    return lista