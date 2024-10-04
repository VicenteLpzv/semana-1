#Vicente Yahir Lopez Vazquez, 240010
print ("Este es el programa para calcular area y perimetro de un triangulo")
# A= b*h/2    P = h+b+c

h= float(input("Ingresa la altura "))
b= float(input("Ingresa la base "))
l= float(input("Ingresa la longitud "))

A = b*h/2
P = h+b+l

print (f"El area es: {A:.2f} y el perimetro es: {P:.2f}")
