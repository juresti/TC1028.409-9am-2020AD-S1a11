cont = 0
sigue = input("Quieres seguir adelante? (si/no) ")
sigue = sigue.lower()
while (sigue == "si"):
    cont += 1
    sigue = input("Quieres seguir adelante? (si/no) ")
    sigue = sigue.lower()
    
print(cont)
    