import os
print(os.getcwd()) #donde está trabajando Thonny

def datos(nombreArch):
    nombre = input("Dime tu nombre: ")
    edad = input("Dime la edad: ")
    edoCivil = input("Dime el estado civil: ")
    lista = [nombre + "\n",edad + "\n",edoCivil + "\n"]
    
    with open(nombreArch + ".txt","w") as miArch:
        miArch.writelines(lista)
    
    print("Archivo guardado en disco")
    print("Guardado en " + os.getcwd())
    
    