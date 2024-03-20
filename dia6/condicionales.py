#CONDICIONAL IF

#if condicion:
#   codigo a ejecutar. Se ingresa tabulado (boton tab o 4 espacios a la derecha)

edad = input("¿Que edad tienes?\n") #17 -> se almacena
edad = int(edad) #edad = int("17")-> edad = 17

#si el usuario es mayor o menor de edad
if edad >= 18:
    print("Eres mayor de edad")
    # print("Programa finalizado") -> no cerraria el programa porque lo consideraria parte del bucle.
    
print("Programa finalizado") #Esto esta fuera del if, por no tener tabulacion

#CONDICIONAL ELSE -> para mas de una opcion como respuesta.

#if condicion:
#   codigo a ejecutar (tabulado a la derecha)
#else:
#   ejecutar siguiente codigo -->se ejecuta en caso de no cumplir se condicion del IF.

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    
print("Programa finalizado")

#CONDICIONAL ELIF -> vuelve a evaluar, para mas de dos opciones como respuesta. Va entre IF y ELSE

#if condicion:
#   codigo a ejecutar (tabulado a la derecha)
#elif (otra condicion):
#   Si se cumple esta nueva condicion ejecuta codigo.
#else:
#   ejecutar siguiente codigo -->se ejecuta en caso de no cumplir se condiciones del IF y ELIF.

if edad > 18:
    print("Eres mayor de edad.")
elif edad == 18:
    print("Felicidades, ya eres mayor de edad.")
else:
    print("Aun eres menor de edad.")
    
print("Programa finalizado")
