def linea(ancho):
    strLinea = ""
    for num in range(ancho):
        #print("*")
        strLinea += "*" #concatenando strings
    #print(strLinea)
    return strLinea
        
def main():
    wide = int(input("Dime el ancho de la linea: "))
    line = linea(wide)
    print(line)
    