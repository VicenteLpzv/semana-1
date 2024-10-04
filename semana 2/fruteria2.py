#Vicente Yahir Lopez Vazquez - 240010
#determinar cuanto pagará una persona que compre manzanas en la fruteria

apple = float(input("Ingresa el precio de la manzana: "))

kg = float(input("Cuantos kilos desea comprar?: "))

if kg <= 2:
    off = 0
   # print (f"El total a pagar es: {total:.2f} pesos")  

elif kg <= 5:
   off = .10
   # total = (apple * kg) *(1 - .10) # *(1 - .10) esto para quitar el 10% de descuento y se agregue directo a "total"
    #print (f"El total a pagar es: {total:.2f} pesos") 

elif kg <= 10:
   off = .15
    #total = (apple * kg) * (1 - .15)
    #print (f"El total a pagar es: {total:.2f} pesos")
     
elif kg >=10.01:
  off = .20
   # total = (apple * kg) * (1 - .20)
    #print (f"El total a pagar es: {total:.2f} pesos") 
    
precio = apple * kg
des = precio * off
total = precio - des

print (f"El total a pagar es: {total:.2f} pesos") 

   
