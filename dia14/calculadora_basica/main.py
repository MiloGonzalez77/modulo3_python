import suma #importar todo de suma
import resta as r #importar todo asignando un alias
from input import captura_datos #Importar metodo/funcion especifica


print(" Calculadora básica\n")
print("Seleccione opcion a realizar")
print("1.- Sumar")
print("2.- Restar")
print("0.- Salir")
opcion = int(input(">  "))

if opcion == 1:
    x , y = captura_datos()
    suma.sumar(x,y)
elif opcion == 2:
    x , y = captura_datos()
    r.restar(x,y)
elif opcion == 0:
    print("Hasta luego, regrese pronto")
else:
    while opcion != 1 or opcion != 2 or opcion != 0:
        print("Opción invalida")

print("Fin de Programa")
