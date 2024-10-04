#Vicente Yahir Lopez Vazquez - 240010

op = str(input("ingresa alguna operacion + - x /: "))
n1 = int(input("Ingresa el primer numero: "))
n2 = int(input("Ingresa el segundo numero: "))
         
if op == "+":
    r=n1+n2
    print(f"La suma es: {r}")
elif op == "-":
    r=n1-n2
    print(f"La resta es: {r}")
elif op == "x":
    r=n1*n2
    print(f"La multiplicacion es: {r}")
elif op == "/":
    r=n1/n2
    print(f"La division es: {r:.2f}")
else:
    print("La operacion ingresada no es valida")
    