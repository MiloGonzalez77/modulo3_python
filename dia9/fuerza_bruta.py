#Actividad 3 - Fuerza bruta

#Determinar cuántos intentos son necesarios para encontrar combinaciones numéricas en minúscula.
from string import ascii_lowercase
import getpass

# contraseña mostrada usada para las pruebas = gato

contrasenia = getpass.getpass("Por favor, ingrese su contraseña:\n").lower()
#variable para contar cantidad de intentos
contador_intentos =0

# For para recorrer contrasenia 
for caracter in contrasenia:
    for char in ascii_lowercase:
        # print(caracter,char)
        if caracter == char:
            contador_intentos =contador_intentos + 1
            break
        else:
            contador  =contador_intentos + 1


print(f"la cantidad de intentos fue: {contador_intentos} intentos")      

print("######## Programa Finalizado #######")