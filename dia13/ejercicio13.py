#FUNCIONES:

from os import system 
"""
    #Funciones - ejemplo sintactico:
    
    def nombre_funcion():
        #codigo a ejecutar
    
    #Por si solo no es visible, a menos que se haga un metodo que le llame a la accion. Dicho metodo debe ser usado despues de la definicion de dicha funcion, usando siempre los "()"
    #Es buena practica definir todas las funciones al inicio del codigo
    #Si una funcion no es invocada, nunca se ejecutara el codigo que contiene. Resultando en codigo muerto.
    
    Parametro: es la variable a utilizar en al funcion.
    Argumento: es el valor que sera entregado en el/la llamado/invocasion.
"""
print("Inicio") #Definicion de la funcion.

def imprimir_menu():
    print("Opciones: ")
    print("1. De acuerdo")
    print("2. En desacuerdo")
    print("3. No me interesa")

imprimir_menu() #Llamado a la funcion.
imprimir_menu()

print("Fin")
print("--------")
system("cls") #Limpiar consola/terminal

def suma(valor1,valor2):
    suma = valor1+valor2
    return suma

def suma2(valor1,valor2):
    return valor1 + valor2
    print("Hola")#nunca se ejecutara.

suma(3,5) #Sin hacer nada con el valor de retorno.
print(f"Valor suma: {suma(3,5)}") #8 -> se imprime el valor de retorno.
resultado = suma(6,7) #capturando el valor de retorno.
print(f"Valor de resultado: {resultado}") #imprime valor de retorno capturado.
print(f"Valor suma2: {suma2(4,7)}") 
print("-------")

#Retornos multiples
def cuadrado_cubo(base):
    cuadrado = base ** 2
    cubo = base  ** 3
    return cuadrado, cubo

print(cuadrado_cubo(2))#retorno de una tupla (4, 8)

valor_cuadrado,valor_cubo = cuadrado_cubo(3)#(9,27)
print(valor_cuadrado,valor_cubo)
print("-------")
