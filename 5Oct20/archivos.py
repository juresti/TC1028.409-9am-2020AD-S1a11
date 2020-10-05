def leeArchivo(nombre):
    miArch = open(nombre + ".txt","r")
    #info = miArch.read() #como string gigante
    info = miArch.readlines() #como lista de strings
    print(info)
    miArch.close()
    
def escribeArchivo(nombre):
    archivo = open(nombre + ".txt","a")
    #archivo.write("Le mando algo para\n que lo escriba")
    lista = ["escribo algo\n","otra linea\n","la ultima\n"]
    archivo.writelines(lista)
    archivo.close()
    print("Archivo escrito a disco")
    