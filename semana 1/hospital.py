#Vicente Yahir Lopez Vazquez - 240010
#Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal.

PresupuestoA = float(input("Ingresa el presupuesto anual del hospital: "))
Ginecologia = PresupuestoA*0.40
traumatologia = PresupuestoA*0.30
pediatria = PresupuestoA*0.30

print (f"El presupuesto anual de Ginecologia es: {Ginecologia:.2f} pesos")
print (f"El presupuesto anual de traumatologia es: {traumatologia:.2f} pesos")
print (f"El presupuesto anual de pediatria es: {pediatria:.2f} pesos")