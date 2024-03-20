nombre = "Camilo"
apellido1 = "González"
apellido2 = "Ulloa"
edad = "33"
#edad = 33 -> se puede declarar pero no concatenar en un print conacatenado con string.
año = 1990
mes = 8
dia = 22
"""
print("***************")
print("Hola " + nombre +" "+ apellido1 +" "+ apellido2 + " - tu edad es " + edad + " años")
print("***************")
"""
print("*******INFORMACIÓN***********************")
print("******** Nombre: " + nombre + " ***********")
print("** Apellido Pat: " + apellido1 + " ********")
print("** Apellido Mat: " + apellido2 + " ********")
print("********** Edad: " + edad + " *************")
print("**** Nacimiento: ",dia, " de ",mes, " de ",año)
print("*****************************************")
#NO SE PUEDE CONTATENAR STRINGS CON NUMEROS EN PYTHON!!!
#Print de string y numeros se puede usando "," de separación

#Interpolacion de cadenas (otra manera de imprimir) -> (f"")
mes = 3
dia = 7
año = 2024

print(f" Hola {nombre}, la fecha es día {dia} del mes {mes} del año {año}.")