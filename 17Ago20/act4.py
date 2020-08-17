import math

#Ejercicio 1
r = float(input("Dime el radio: "))
area = 4 * math.pi * r ** 2
vol = (4 * math.pi * r ** 3) / 3
print(f"El area del radio {r} es {area:.4f}")
print(f"El volumen del radio {r} es {vol:.2f}")
