#Vicente Yahir Lopez Vazquez - 240010
#Crear un programa que pida al usuario los tres lados de un triángulo y
#determine si es equilátero, isósceles o escaleno.

l1 = float(input("ingresa lado 1: "))
l2 = float(input("ingresa lado 2: "))
l3 = float(input("ingresa lado 3: "))

if l1 == l2 == l3:
    print("El triángulo es equilátero.")
elif l1 != l2 and l3 != l2 and l1 != l3:
    print("El triángulo es escaleno.")
else:
    print("El triángulo es isósceles.")