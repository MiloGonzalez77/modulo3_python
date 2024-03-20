import sys
buscar = sys.argv[1] # número a ingresar por consola a buscar
import random
lista = [1,2,3,4,5,6,7,8,9,0]
# .shuffle de la librería random permite mezclar
# la lista de dígitos para aumentar un poco la dificultad.
random.shuffle(lista)

# revisaremos cada elemento en la lista
# también llevamos registro de la posición en la que estamos
for position, elemento in enumerate(lista): #-> Entrega posicion, para no usar contador
# Si el elemento es igual a lo que buscamos terminamos el ciclo
    if elemento == buscar:
        print("¡Elemento encontrado! Se terminará del ciclo")
        break
    else:
        # Si es que no es el elemento buscado lo reportamos
        print("Elemento no encontrado")

print("Ha terminado el ciclo")
print(f'El elemento {buscar} se encontró en la posición {position}')
print(f'La lista mezclada es: {lista}')

print("------")
