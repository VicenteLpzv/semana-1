#Vicente Yahir Lopez Vazquez - 240010
#El dueño de una tienda compra un artículo a un precio determinado. 
#Determinar el precio en lo que lo debe vender para obtener una ganancia del 30%.
articulo = float(input("Ingresa el precio del articulo que deseas comprar: "))
ganancia = articulo*0.30
vender = articulo + ganancia
print (f"para ganar el 30%, debes vender el articulo a: {vender:.2f} pesos")
