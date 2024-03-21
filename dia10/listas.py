#LISTAS
"""
    Pueden contener distitos tipos de elementos.
    Son mutables.
    usan [] para definir variables de tipo lista.
    los datos se agrupan separados por "," y en orden de ingreso.
    índice => posicion de los elementos de la lista. En python se ordenan desde 0 al n-1. 
    donde, la primera pos. es 0 y la ultima n-1 (cantidad_elementos - 1)
    Para acceder a los elementos utilizamos al sposiciones.
    En python no pueden quedar indices vacios en las listas.
    
    En Python, cuando asignas una lista a otra variable utilizando el operador de asignación (=), 
    estás creando una nueva referencia a la misma lista en la memoria, no una nueva lista. Por lo tanto, 
    ambas variables (lista1 y lista2) apuntan a la misma ubicación de memoria, lo que significa que cualquier cambio 
    realizado en una de las variables también afectará a la otra.
    
    Los metodos con __nombre__ se lllaman "magic buildt-in" o "dunders"
"""

lista1 = [1,2,3,4]
print(f"Lista 1: {lista1}")
print("-------")
print(f"Nueva lista: {[1, 2, 'hola', 4]}")
print("-------")

colores = ["verde", "rojo", "rosa", "azul"] #tiene 4 elementos .> ult pos. es: 4-1 -> 3.
print(f"Pos. 0: {colores[0]}") #verde
print(f"Pos. 1: {colores[1]}") #rojo
print(f"Pos. 2: {colores[2]}") #rosa
print(f"Pos. 3: {colores[3]}") #azul
#print(f"Pos. 4: {colores[4]}") --> Arroja error de index -> fuera de rango
print(f"Pos. -1: {colores[-1]}") #azul
print(f"Pos. -2: {colores[-2]}") #rosa
#print(f"Pos. -2: {colores[-5]}") --> tambien da error fuera de rango

print("-------")

###METODOS CON LISTAS.
#lista.metodo()

print(colores.__dir__()) #mostrar todos los metodos que contiene la lista en especifico.
print("-------")

#Metodo append()
colores.append("amarillo") #append() -> Agrega elemento a la lista
print(f"Lista colores: {colores}")
print("-------")

#Metodo insert()
colores.insert(0,"blanco") #inserta en una pos especifica, y si estaba utilizada por otro elemento, éste y los demas elementos se desplazan una posicion
print(f"Lista colores: {colores}")
print("-------")
colores.insert(6,"negro") #Inserta en pos 6, como no habia elemento antes se ubica al final.
print(f"Lista colores: {colores}")
print("-------")

colores.insert(18,"cafe") #Agregar en índice fuera de rango, lo asigan automaticamente en la ultima disponible
print(f"Lista colores: {colores}")
print("-------")

colores.insert(-4,"fucsia") #Agregar en índice negativo agrega contando desde la ultima posicion y desplaza el elemento que estaba antes.
print(f"Lista colores: {colores}")
print("-------")

#Metodo pop([indice]) -> elimina un elemento desntro de la lista
colores.pop(3) #Elimina color rosa, y desplaza el resto de la lista para cubrir el indice vacio.
print(f"Lista colores: {colores}")
print("-------")

colores.pop(-2) #Elimina color negro, y desplaza el resto de la lista para cubrir el indice vacio.
print(f"Lista colores: {colores}")
print("-------")

colores.insert(0,"cafe") 
print(f"Lista colores: {colores}")

#Metodo remove()
colores.remove("cafe") #remueve el primer elemento de la lista que encuentra con el mismo nombre. Independiente si hay mas con el mismo nombre.
print(f"Lista colores: {colores}") 
print("-------")
#colores.remove("cafes") ###.> ValueError: list.remove(x): x not in list Si nombre del elemento a removar no existe, arrohja error de valor.

print(f"Lista colores: {colores}") #['cafe', 'blanco', 'verde', 'rojo', 'fucsia', 'azul', 'amarillo', 'cafe']
#Metodo reverse() --> invierte los indices de los elementos.
colores.reverse() #Ojo, que el cambio que genera es permanente.
print(f"Lista colores: {colores}") #['cafe', 'amarillo', 'azul', 'fucsia', 'rojo', 'verde', 'blanco']
print("-------")

#Metodo sort() -> Organiza los elemento de manera alfabetica ascendente
colores.sort() #Tambien hace cambio permanente
print(f"Lista colores: {colores}") #['amarillo', 'azul', 'blanco', 'cafe', 'fucsia', 'rojo', 'verde']
print("-------")

lista2 = lista1 #Esto NO es un respaldo de la lista
lista3 = lista1.copy() #Si es un respaldo de los datos.
lista4 = lista1[:] #Esto tambien es un respaldo de los datos (metodo slice).
lista5 = list(lista1) #Tambien es un respaldo de los datos.
lista7 = lista1 + [] # Tambien reslpada, pero no es la mejor forma.

print(f"Lista 2: {lista2}")
lista2.append(5)
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3: {lista3}")
print(f"Lista 4: {lista4}")
print(f"Lista 5: {lista5}")

#Metodo sorted(lista,reverse=True) ->Ordena de manera descendente
print(sorted(colores,reverse=True)) # ['verde', 'rojo', 'fucsia', 'cafe', 'blanco', 'azul', 'amarillo'] --> no es permanente
print(sorted(colores)) # ['amarillo', 'azul', 'blanco', 'cafe', 'fucsia', 'rojo', 'verde'] --> de manera ascendente.
print(f"Lista colores: {colores}") # ['amarillo', 'azul', 'blanco', 'cafe', 'fucsia', 'rojo', 'verde']
print("-------")

#Metodo index() -> retorna el indice (positivo) del elemento, siemrpre que lo encuentre.
print(colores.index('azul')) # 1
print(colores.index('rojo')) # 5
# print(colores.index('negro')) # ValueError: 'negro' is not in list - no existe

#Metodo clear()
"""
    colores.clear() # -> borra todos los elementos de la lista.
    print(colores) # [] -> Lista vacia.
"""

###OPERACIONES###
lista6 = [20,30,40,50]
lista_concatenada = lista1 + lista6
print(f"Lista 1; {lista1}")
print(f"Lista 6; {lista6}")
print(f"Lista 7; {lista7}")

print(f"Lista concatenada; {lista_concatenada}")
lista6.append(60)
print(lista_concatenada)
