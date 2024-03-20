#NUMEROS PARES E IMPARES

#Solicitar valor interactivo:}
numeroAevaluar = int(input("Intgrese un numero entero\n"))

#Determinar si es par o impar. utilizando modulo o resto de la division.
if numeroAevaluar%2 == 0:
    print("El numero ingresado es PAR.")
else:
    print("El numero ingresado es IMPAR.")
print("Fin de programa")

#Si quisieramos capturar 0 a parte.
if numeroAevaluar == 0:
    print("El numero ingresado es 0")
elif numeroAevaluar%2 == 0:
    print("El numero ingresado es PAR.")
else:
    print("El numero ingresado es IMPAR.")
print("Fin de programa")
