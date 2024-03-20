#DESAFIO IMC
#Formula IMC = PESO (en kilos) / ESTATURA (en metros) ** 2

#Pedir y validar peso en kgs
pesoEnKilos = float(input("Ingrese su peso en Kilogramos - Ej: 50.0\n"))

if pesoEnKilos <= 0.00:
    print("Error, el peso ingresado no puede ser igual o menor que 0.00")
    print("Fin de programa")
    quit() #salir del programa.
elif pesoEnKilos > 500.0:
    print("Error, datos no válidos!")
    print("Fin de programa")
    quit() #salir del programa.
else:
    print(f'Su peso es de {round(pesoEnKilos,2)} kgs.')

#pedir y validar estatura en cms y convertir en metros
estaturaEnCentimetros = int(input("Ingrese su estatura en centimetros - Ej: 150\n"))
if estaturaEnCentimetros <= 0:
    print("Error, la estatura ingresada no puede ser igual o menor que 0")
    print("Fin de programa")
    quit()
elif estaturaEnCentimetros > 0 and estaturaEnCentimetros <= 250:
    print(f'Su estatura es de {estaturaEnCentimetros} cms')
else:
    print("Error, datos no válidos!")
    print("Fin de programa")
    quit()
    
#Calcular e imprimir IMC
estaturaEnMetros = float(estaturaEnCentimetros/100)
imc = pesoEnKilos/(estaturaEnMetros**2)
print(f'Su Indice de Masa corporal es del {round(imc,1)}%.')

#Comparar condicion IMC e imprimir clasificacion
if imc < 18.5:
    print("Resultado: Su clasificacion OMS es Bajo Peso")
elif imc >= 18.5 and imc < 25:
    print("Resultado: Su clasificacion OMS es Adecuado")
elif imc >= 25.0 and imc < 30.0:
    print("Resultado: Su clasificacion OMS es Sobrepeso")
elif imc >= 30.0 and imc < 35.0:
    print("Resultado: Su clasificacion OMS es Obesidad Grado I")
elif imc >= 35.0 and imc < 40.0:
    print("Resultado: Su clasificacion OMS es Obesidad Grado II")
else:
    print("Resultado: Su clasificacion OMS es Obesidad Grado III")

print("Programa finalizado")