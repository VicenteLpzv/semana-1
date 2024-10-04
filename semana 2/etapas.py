#Vicente Yahir Lopez Vazquez - 240010
#Calcular la diferencia entre dos enteros positivos
#Crear un programa que pida al usuario su edad y le indique a qué grupo
#etario pertenece. Puedes definir tus propios rangos de edad.

edad = int(input("Ingresa tu edad: "))

if edad <= 6:
    print("Tu edad pertenece al grupo infantil")
elif edad <=12:
    print("Tu edad pertenece al grupo de la niñez")
elif edad <=20:
    print("Tu edad pertenece al grupo de la adolescencia")
elif edad <=25:
    print("Tu edad pertenece al grupo de la juventud")
elif edad <=60:
    print("Tu edad pertenece al grupo de la adultez")
elif edad >=60:
    print("Tu edad pertenece al grupo de la ancianidad")
else:
    print("Edad no válida")
