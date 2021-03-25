hproductos = input("Ingresa la entalpía de los productos: ")
sproductos = input("Ingresa la entropía de los productos: ")
tproductos = input("Ingresa la temperatura de los productos (en Kelvin): ")
hreactivos = input("Ingresa la entalpía de los reactivos: ")
sreactivos = input("Ingresa la entropía de los reactivos: ")
treactivos = input("Ingresa la temperatura de los reactivos (en Kelvin): ")

print("La diferencia de entalpía es: ",str(hproductos-hreactivos))
print("La diferencia de entropía es: ",str(sproductos-sreactivos))
print("La diferencia de temperatura es: ",str(tproductos-treactivos))
print("La energía libre de Gibbs es: ","")#Calcular la energía libre de gibbs