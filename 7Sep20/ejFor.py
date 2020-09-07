def escalera(num):
    salida = ""
    for num in range(1,num + 1):
        salida += str(num) + ","
        
    for num in range(num - 1,1,-1):
        salida += str(num) + ","
    print( salida + "1")