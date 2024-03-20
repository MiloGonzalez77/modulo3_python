import math

#Inputs de datos
r = float(input("Ingrese el radio del planeta en kilometros: \n"))
g = float(input("Ingrese la constante de gravedad del planeta en metros: \n"))

#Calculo
vEscape = math.sqrt(2*g*(r*1000))

#salida
print(f'La velocidad de escape es: {round(vEscape, 1)} [m/s]')