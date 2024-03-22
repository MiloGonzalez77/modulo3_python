tupla_eje = ("marzo","2024")
print(tupla_eje) #('marzo', '2024')
print(type(tupla_eje)) #<class 'tuple'>

#desempaquetamiento
mes, anio = tupla_eje
print(mes)
print(anio)

tupla2 = 3,5,7,9
print(type(tupla2)) #<class 'tuple'>
print(tupla2) #(3, 5, 7, 9)

lista_vocales = ["a","e","i","o","u"]
print(lista_vocales) #['a', 'e', 'i', 'o', 'u']
tupla_vocales = tuple(lista_vocales)
print(tupla_vocales) #('a', 'e', 'i', 'o', 'u')
print("-------")

#Iterar tupla
for tv in tupla_vocales:
    print(tv)

#Count cuenta las veces que esta un mismo elmento en la tupla
print(tupla_vocales.count("a")) #1

###Sets
"""Sets:
    se escriben con {}, no tienen clave (solo valores), no permite datos repetidos.
    No tienen un orden especifico (cambian en cada ejecucion).
    Sirve para trabajar con conjuntos de datos unicos. Por lo que no acepta listas ni diccionarios ni set anidado.
"""
muchos_animales = {
    'Gato', 'Perro', 'Tortuga', 
    'Gato', 'Perro', 'Tortuga', 
    'Gato', 'Perro', 'Tortuga', 
    'Gato', 'Perro', 'Tortuga', 
    'Hurón', 'Hamster', 'Erizo de Tierra',10,12
    }
print(muchos_animales) #{'Tortuga', 'Erizo de Tierra', 'Hamster', 10, 12, 'Hurón', 'Gato', 'Perro'}
print("--------")
muchos_animales.add(7)
print(muchos_animales) #lo agrega en cualquier parte.
muchos_animales.remove(10) #si no lo pilla, se cae.
muchos_animales.discard("Raton") #si no lo encuentra no hace nada.
muchos_animales.discard("Hurón") #si lo pilla lo borra.
muchos_animales.pop() #si no se espicifica elimina un elemento cualquiera.
print(muchos_animales)
muchos_animales.clear() #borra el contenido de set. set vacio
print(muchos_animales) #set()
print("--------")

##Convertir un diccionario en una lista
lista_diccionario = list({"k1": 5, "k2": 7}.items()) # [('k1', 5), ('k2', 7)]
print(lista_diccionario) #[('k1', 5), ('k2', 7)]
print("")
print(lista_diccionario[0])#accedemos a la posicion de lista -> ('k1', 5)
print(lista_diccionario[0][0])#accedemos a lista y a posicion de tupla. -> k1
print(lista_diccionario[0][1])#accedemos a lista y a posicion de tupla. -> 5
print("")
print(lista_diccionario[1]) #('k2', 7)
print(lista_diccionario[1][0]) #k2
print(lista_diccionario[1][1]) #7
print("-------")

##Convertir una lista en diccionario
diccionario_lista = dict([('k1', 5), ('k2', 7)]) # {"k1": 5, "k2": 7}
print(diccionario_lista)
print("-------")

##Funciones
#dir
print(f"lista: {dir(lista_diccionario)}") #muestra en lista de str todos los metodos que podemos usar en la lista
print(f"tupla: {dir(tupla2)}") #muestra lista de metodos para una tupla.
print("--------")

