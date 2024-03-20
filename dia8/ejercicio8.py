#for each
"""
    for variable in iterable:
"""

#funcion range()
#valor de inicio es el 0. ->[0-10[ ->el ultimo numero no es considerado.
for i in range(10):
    print(i)
print("------")
for i in range(4,10): #[4-10[ ->4 es el valor de inicio
    print(i)
print("------")
for i in range(4,10,3): #-> [4-10[ de 3 en 3 desde el 4. -> el tercer valor es la frecuencia de iteracion.
    print(i)
print("------")
for i in range(0,21,2): #-> numeros del 0 al 20 mostrando numeros pares.
    print(i)
print("------")
for i in range(1,21): #-> numeros de 1 al 20 mostrando numeros pares.
    if i % 2 == 0:
        print(i)
print("------")
#lo anterior pero con while
i=1
while i <= 20:
    if i%2 == 0:
        print(i)
    i+=1
print("-------")
#Lo mismo anterior pero con menos codigo y sin verificar
i = 0
while i <= 20:
    print(i)
    i+=2
print("------")

#LISTAS ITERABLES -> Conjunto de datos ordenados segun su ingreso separado por coma, en un mismo contenedor. El primero está en posicion 0.
lista = [1,5,8,3,4]

for elemento in lista: #elemento = 1
    print(elemento)
print("------")

#String son considerados objetos iterables. Similar a las listas, pero sin separacion por comas.
texto = "Hola mundo!!"
for caracter in texto:
    print(caracter)
print("------")

#Recordando lista cachipu:
opciones = ['piedra','papel','tijeras']
for opcion in opciones:
    print(opcion)
print("------")

"""
    Diccionario {clave : valor, clave : valor, etc.}
    No existen las posiciones, como en las listas
"""
diccionario = {
    "Nombre": "Carlos",
    "Apellido": "Santana",
    "Ocupacion": "Guitarrista"
}
print("---Print diccionario---")
for clave in diccionario:
    print(clave)
print("")
for clave in diccionario: #para obtener claves y valores
    print(f"clave {clave} - valor {diccionario[clave]}")
print("")
for valor in diccionario.values(): #Solo para obtener valores de las claves
    print(f"El valor es {valor}")
print("")
for clave, valor in diccionario.items(): #Hace lo mismo que en linea 70.
    print(f"clave {clave} - valor {valor}")
print("------")

#Tabla de multiplicar (tabla del 5)
for numero in range(10):
    print(f"5 * {numero} = {5 * numero}")

#ahora todas las tablas del 0 al 9.
for numero1 in range(10):
    print(f'\nTabla del {numero1}:------------------------------\n')
    for numero2 in range(10):
        print(f"{numero1} * {numero2} = {numero1*numero2}")
print("------")

"""
for (let index = 0; index < 10; index++) {
    console.log(index)
    } -->javascript.
    """
#For para ciclos limitados
for index in range(0,10,1):
    print(f"Indice {index}")
print("Fin programa")