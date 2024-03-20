#Input de datos
precioSuscripcionNormal = float(input("Ingrese el precio del servicio normal en clp: \n"))
cantidadUsuariosNormales = int(input("Ingrese la cantidad de usuarios normales: \n"))
precioSuscripcionPremium = float(input("Ingrese el precio del servicio premium en clp: \n"))
cantidadUsuariosPremium = int(input("Ingrese la cantidad de usuarios premium: \n"))
gastosTotales = float(input("Ingrese los gastos totales en clp: \n"))

#Calculo -> utilidades = p * u - gt
utilidades = precioSuscripcionNormal * cantidadUsuariosNormales + precioSuscripcionPremium  * cantidadUsuariosPremium - gastosTotales

#salida utilidades
print(f'Las utilidades son: ${round(utilidades,1)} ')

#Input utilidades año anterior
utilidadAnioAnterior = float(input("Ingrese utilidades mayor a 0 del año anterior en clp: \n"))

#validacion de variables (condicional)
if utilidadAnioAnterior > 0:
    #realizar lo que está tabulado
    #calculo de razon
    razonUtilidades = utilidades/utilidadAnioAnterior
    #Salida
    print(f'La razon de utilidad respecto al año anterior es de: {round(razonUtilidades,2)}')
else:
    #realizar accion por default
    print("Las utiliudades no pueden ser iguales o menores a cero")
    