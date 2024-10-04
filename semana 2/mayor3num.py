#Vicente Yahir Lopez Vazquez - 240010
#Encontrar el mayor entre tres números

n1 = int(input("Ingresa un numero: "))
n2 = int(input("Ingresa un 2do numero: "))     
n3 = int(input("Ingresa el 3er numero: "))
max = n1
if n1 > n2 and n1 > n3:
    max=n1
   
elif n2 > n3:
    max=n2
    
else:
    max=n3
    
print ( f" {max}  es mayor")
    
   

    

