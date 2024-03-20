#IMC

import sys
peso_kilogramos= float(sys.argv[1])
estatura = float(sys.argv[2])/100

print(sys.argv)     #['.\\dia6\\imcConArgumentosResueltoEnClase.py', '81', '178']
print(sys.argv[1])  #81
print(sys.argv[2])  #178

#Validacion peso en kilogramos
if peso_kilogramos <= 0.00:
    print("Error, el peso ingresado no puede ser igual o menor que 0.00")
    print("Fin de programa")
    quit() #salir del programa.
elif peso_kilogramos > 500.0:
    print("Error, datos no válidos!")
    print("Fin de programa")
    quit() #salir del programa.
else:
    print(f'Su peso es de {round(peso_kilogramos,2)} kgs.')

#Validacion estatura
if estatura <= 0:
    print("Error, la estatura ingresada no puede ser igual o menor que 0")
    print("Fin de programa")
    quit()
elif estatura > 0 and estatura <= 250:
    print(f'Su estatura es de {estatura} mts')
else:
    print("Error, datos no válidos!")
    print("Fin de programa")
    quit()

#Calculo IMC
imc = peso_kilogramos/(estatura**2)
print(f'Su Indice de Masa corporal es del {round(imc,1)} %.') #":." funciona igual que "round(variable,decimal)""

#Comparar condicion IMC e imprimir clasificacion
if imc > 0 and imc < 18.5:
    clasificacion = "Bajo Peso"
elif imc < 25:
    clasificacion = "Adecuado"
elif imc < 30.0:
    clasificacion = "Sobrepeso"
elif imc < 35.0:
    clasificacion = "Obesidad Grado I"
elif imc < 40.0:
    clasificacion = "Obesidad Grado II"
elif imc >= 40.0:
    clasificacion = "Obesidad Grado III"
else:
    print("datos no validos, imc no puede ser menor a cero")
    quit()

print(f'Resultado: Su clasificacion OMS es {clasificacion}')
print("Programa finalizado")