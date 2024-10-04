#Vicente Yahir Lopez Vazquez - 240010
#Escribir un programa que pida al usuario dos números enteros

n = (input("ingresa un numero entero: ")) #dividendo
m = (input("Ingresa otro numero entero: ")) #divisor

div=str(int(n)//int(m))
residuo=str(int(n)%int(m))

print (f" {n} entre {m} da un cociente de {div} y un resto de {residuo} ")