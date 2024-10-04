#Vicente Yahir Lopez Vazquez - 240010
#programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable,

peso = float(input("Ingrese su peso en kg: "));
altura = float(input("ingrese su altura en metros: "));

imc = peso/(altura*altura)

print (f"Tu indice de masa corporal es: {imc:.2f}")