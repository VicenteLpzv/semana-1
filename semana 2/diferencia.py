#Vicente Yahir Lopez Vazquez - 240010
#Calcular la diferencia entre dos enteros positivos

n1 = int(input("Dame un numero: "));
n2 = int(input("dame otro numero: "));

op = (n1 - n2) ** 2
dif = op **0.5 #raiz cuadrada de op

if n1 > 0 or n2 > 0:
    print (f"{dif:.0f}")
    

    



