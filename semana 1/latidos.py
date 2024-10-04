#Vicente Yahir Lopez Vazquez - 240010
#Calcular el número de ejercicios que una persona debe tener por cada 10
#segundos/día de ejercicio, si la fórmula es la siguiente: (220 - edad) / 10

edad = int(input("Ingresa edad: "))
latidos = (220 - edad) / 10

print (f"Tus latidos en 10 segundos son: {latidos:.2f}")



