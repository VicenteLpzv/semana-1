

print ("Programa que solicita la edad del usuario y este imprima si es o no es mayor de edad")

try:
    edad = int(input("Ingresa tu edad: "))
except ValueError:
    print ("Debes ingresar un numero valido (mayor a 0).")
    exit()
    
 
if edad >= 18:
        print ("eres de mayor de edad");
else:
        print ("eres menor de edad");