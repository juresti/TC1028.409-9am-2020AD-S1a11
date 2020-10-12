import os
print(os.getcwd())

def listaLimpia(lista):
    """Recibe una lista con \n y
    la regresa limpia de \n"""
    for pos in range(len(lista)):
        lista[pos] = lista[pos].rstrip()
        
    return lista
        

def consultaArchivo(nomArch):
    with open(nomArch + ".txt","r") as arch:
        registros = arch.readlines()
        
    registros = listaLimpia(registros)
    #print(registros)
    numReg = len(registros) // 3
    pos = 0 #posición inicio de registro
    for cont in range(numReg):
        print(f"DATOS DEL REGISTRO {cont + 1}")
        print(f"Nombre: {registros[pos]}")
        print(f"Edad: {registros[pos+1]}")
        print(f"Estado civil: {registros[pos+2]}\n")
        
        pos += 3

def consultaUnRegistro(numReg,nomArch):
    """Recibe el numero de registro que desea consultar.
    Lo imprime y regresa también la lista con esa información"""
    with open(nomArch + ".txt","r") as arch:
        registros = arch.readlines()
        
    registros = listaLimpia(registros)
    
    numReg -= 1 #Empieza en cero
    pos = numReg * 3 #3 elementos por registro
    print(f"DATOS DEL REGISTRO {numReg+1}")
    print(f"Nombre: {registros[pos]}")
    print(f"Edad: {registros[pos+1]}")
    print(f"Estado civil: {registros[pos+2]}\n")
    
    return [registros[pos],int(registros[pos+1]),registros[pos+2]]
