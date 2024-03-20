#Inputs de datos
precio = int(input("Ingrese el precio del servicio en clp: \n"))
cantidadUsuarios = int(input("Ingrese la cantidad de usuarios: \n"))
gastosTotales = int(input("Ingrese los gastos totales en clp: \n"))

#Calculo -> utilidades = p * u - gt
utilidades = precio * cantidadUsuarios - gastosTotales

#salida
print(f'Las utilidades son: ${utilidades} ')