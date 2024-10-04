#Vicente Yahir Lopez Vazquez - 240010
#Invertir un número de tres dígitos

A = int(input("Ingresa un numero del 1 al 999: "))


if A > 1 and A <999:
    unidad = A % 10 #obtener residuo de division, unidad =
    decena = (A // 10) % 10 #obtener cociente entero y residuo de division, decena = 
    centena = A // 100 #obtener cociente entero de la division, centena = 
    invertido = unidad*100 + decena*10 + centena
    print(f"El numero invertido es: {invertido}")
else:
     print("El numero debe ser un numero del 1 al 999")
    