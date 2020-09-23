def personas(numPer):
    nombres = [""] * numPer
    for cont in range(numPer):
        nombres[cont] = input(f"{cont+1}. Dime el nombre: ")
    return nombres
    
def personas2(numPer):
    nombres = []
    for cont in range(numPer):
        nombre = input(f"{cont+1}. Dime el nombre: ")
        nombres.append(nombre)
    #print(nombres)
    return nombres

def imprimePersonas(listaPer):
    for persona in listaPer:
        print(persona)
        
def imprimePersonas2(listaPer):
    salida = ""
    for persona in listaPer:
        salida += persona + "\t"
    print(salida)
