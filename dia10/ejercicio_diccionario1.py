"""
    #Practiquemos!
    1. Crea un diccionario
    1. Agrega un elemento
    1. Cambia un elemento
    1. Elimina un elemento
"""

#Crear diccionario
genero = {
    "Juan" : "hombre",
    "Juana" : "mujer",
    "Pepe" : "hombre"
}

print(genero) # {'Juan': 'hombre', 'Juana': 'mujer', 'Pepe': 'hombre'}

#Agregar 1 elemento
genero["Botota"]= "transgenero"
print(genero) # {'Juan': 'hombre', 'Juana': 'mujer', 'Pepe': 'hombre', 'Botota': 'transgenero'}

#Cambiar 1 elemento
genero["Botota"]= "mujer"
print(genero) # {'Juan': 'hombre', 'Juana': 'mujer', 'Pepe': 'hombre', 'Botota': 'mujer'}

#Eliminar 1 elemento
eliminar = genero.pop("Botota")
print(eliminar) # mujer
print(genero) # {'Juan': 'hombre', 'Juana': 'mujer', 'Pepe': 'hombre'}
print("-------")
