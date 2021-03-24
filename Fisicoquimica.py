# Eva, Hugo, Andrea, Kristen
# Fisicoqu ́ımica


def ingreso():
    while True:
        try:
            entropia = int(input("Por favor ingrese la entropia: "))
            entalpia = int(input("Por favor ingrese la entalpia: "))
            temperatura = int(input("Por favor ingrese la temperatura en Kelvins: "))
            return (entropia, entalpia,temperatura)

        except:
            print("Valor incorrecto intente de nuevo")


def delta(uno, dos):
    diferencia =  dos - uno
    return (diferencia)


def gibbs(deltaH, deltaS, temperatura):
    delta_gibbs = deltaH - temperatura*deltaS
    return (delta_gibbs)


# ingreso de datos reactivos
print("Ingreso de datos de los reactivos de la reaccion:")
print("*"*50)
entropia, entalpia, temperatura = ingreso()

#ingreso de datos productos
print("Ingreso de datos de los productos de la reaccion:")
print("*"*50)

#calculos
entropia2, entalpia2, temperatura2 = ingreso()
delta_entalpia= delta(entalpia, entalpia2)
delta_entropia= delta(entropia, entropia2)
delta_gibbs = gibbs(delta_entalpia, delta_entropia, temperatura)

#resultados
print("*"*50)
print("Resultados:")
print("*"*50)
print("ΔH: " + str(delta_entalpia))
print("ΔS: " + str(delta_entropia))
print("ΔG: " + str(delta_gibbs))
