#Vicente Yahir Lopez Vazquez - 240010
#Escribir un programa que lea el número de payasos ybmuñecas vendidos en el último pedido y 
#calcule el pesobtotal del paquete que será enviado.
#b. ¿Cuánto se cobrará de envío, si la paquetería cobra 120 pesos por cada 600g?
#payaso 112g - muñeca 75g

Ppayaso = (112)
Pmuñeca = (75)
costo_600g = (120)

payasos = int(input("ingresa cuantos payasos se vendieron: "))
muñecas = int(input("ingresa cuantas muñecas se vendieron: "))


paquete = (payasos*Ppayaso) + (muñecas*Pmuñeca)
envio = float(paquete // 600) * costo_600g
print (f"El peso del paquete será de: {paquete:.2f} gramos")
print (f"El costo de envio será de: {envio:.2f} pesos")