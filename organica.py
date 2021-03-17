# Universidad del Valle de Guatemala
# Química Computacional
# Grupo 3: Luis, Jenni, Joan, Esteban
# organica.py

def calcIDH(c,h,n):
	return c-h/2+n/2+1

def isNum(x):
	try:
		x = int(x)
		return True
	except:
		return False

valid = False

while not valid:
	c = input('\nIngrese el numero de Carbonos: ')
	valid = isNum(c)
valid = False

while not valid:
	h = input('\nIngrese el numero de Halogenos/hidrogenos: ')
	valid = isNum(h)
valid = False

while not valid:
	n = input('\nIngrese el numero de Nitrogenos: ')
	valid = isNum(n)
valid = False

idh = calcIDH(int(c),int(h),int(n))

print('\nLa cantidad de insaturaciones de la molecula es:',idh)
print('\n')