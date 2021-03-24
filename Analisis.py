from math import log10
VHac = input("Ingrese el valor del volumen de acido acetico agregado: ")
CHac = input("Ingrese la concentracion del acido acetico agregado: ")
VAgua = input("Ingrese el volumen de agua donde se agrega el ácido: ")
VHac = float(VHac)
CHac = float(CHac)
VAgua = float(VAgua)
CNueva = (VHac*CHac)/(VHac+VAgua)
print ("pH =" , -log10(CNueva))
