#DESAFIO CACHIPUN

#Importar funncion choice.
from random import choice

#definir lista de opciones
opcionesCachipun = ['piedra', 'papel', 'tijera']

#Pedir al jugador que juegue entre: piedra, papel o tijeras. Y validar que sea una de esas opciones
turnoJugador = input("Escriba una opción: piedra - papel - tijera\n").lower()

#Print turno jugador:
if turnoJugador != 'piedra' or turnoJugador != 'papel' or turnoJugador != 'tijera':
    print("Opción no válida!")
    print(f'Debes escribir solo una de las siguientes opciones: {opcionesCachipun}')
    print("Fin de program, inicia de nuevo")
    quit()
else:
    print("dato ingresado correctamente")
    print(f'Haz jugado [{turnoJugador}]!')

#Turno computador:
print("Es el turno del computador...")
turnoComputador = choice(opcionesCachipun)
print(f'Computador ha jugado [{turnoComputador}]!')

#comparar y mostrar quien gana o si es empate.
if turnoJugador == 'piedra' and turnoComputador == 'piedra':
    print("Resultado: Empate!")
elif turnoJugador == 'piedra' and turnoComputador == 'papel':
    print("Resultado: Perdiste!")
elif turnoJugador == 'piedra' and turnoComputador == 'tijera':
    print("Resultado: Ganaste!")
elif turnoJugador == 'papel' and turnoComputador == 'piedra':
    print("Resultado: Ganaste!")
elif turnoJugador == 'papel' and turnoComputador == 'papel':
    print("Resultado: Empate!")
elif turnoJugador == 'papel' and turnoComputador == 'tijera':
    print("Resultado: Perdiste!")
elif turnoJugador == 'tijera' and turnoComputador == 'piedra':
    print("Resultado: Perdiste!")
elif turnoJugador == 'tijera' and turnoComputador == 'papel':
    print("Resultado: Ganaste!")
elif turnoJugador == 'tijera' and turnoComputador == 'tijera': #Esta condicion podría haber sido "else:" sin condicion, pero queria dejar clara las 9 posibilidades del juego.
    print("Resultado: Empate!")

print("Programa finalizado con exito!")
