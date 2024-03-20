#Input de datos
precioSuscripcion = float(input("Ingrese el precio del servicio normal en clp: \n"))
cantidadUsuariosNormales = int(input("Ingrese la cantidad de usuarios normales: \n"))
cantidadUsuariosPremium = int(input("Ingrese la cantidad de usuarios premium: \n"))
gastosTotales = float(input("Ingrese los gastos totales en clp: \n"))

#Calculo -> utilidades = p * u - gt
utilidades = precioSuscripcion * cantidadUsuariosNormales + (precioSuscripcion * 1.5)  * cantidadUsuariosPremium - gastosTotales

#salida
print(f'Las utilidades son: ${round(utilidades,1)} ')