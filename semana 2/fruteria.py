#Vicente Yahir Lopez Vazquez - 240010
#determinar cuanto pagará una persona que compre manzanas en la fruteria

apple = float(input("Ingresa el precio de la manzana: "))

kg = float(input("Cuantos kilos desea comprar?: "))

if kg >= 0 and kg <= 2:
    total = kg * apple
    print (f"El total a pagar es: {total:.2f} pesos")  

elif kg >= 2.01 and kg <= 5:
    total = (apple * kg) *(1 - .10) # *(1 - .10) esto para quitar el 10% de descuento y se agregue directo a "total"
    print (f"El total a pagar es: {total:.2f} pesos") 

elif kg >=5.01 and kg <= 10:
    total = (apple * kg) * (1 - .15)
    print (f"El total a pagar es: {total:.2f} pesos")
     
elif kg >=10.01:
    total = (apple * kg) * (1 - .20)
    print (f"El total a pagar es: {total:.2f} pesos") 

   
