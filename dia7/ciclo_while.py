#CICLO WHILE

#Ejemplo password
import getpass

password = getpass.getpass("Ingresa tu contrasenia\n")
#print(f"La contrasenia ingresada es: {password}")

#si usuario escribe "hola" deberia pedir la contraseña otra vez
while password != "hola mundo":
    password = getpass.getpass("Error, ingresa de nuevo la contrasenia!\n")

print("Contrasenia Coreecta!")
print("Programa finalizado.")

#while para pedir que ingrese numero hasta que ingrese el numero 33
numero = int(input("Ingrese un numero del 1 al 100\n"))

while numero <1 or numero >100:
    numero = int(input("Numero no válido, ingrese un numero entero del 1 al 100\n"))

while numero != 33:
    numero = int(input("Ingrese otro numero del 1 al 100\n"))

print("Fin de programa numeros")

#ejemplo while para poner fin:
inicio = 0
fin = 6

while inicio < fin:
    print(f" inicio {inicio} , fin {fin}")
    inicio = inicio + 1

print("Fin de programa")
