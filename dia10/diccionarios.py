###DICCIONARIOS###
"""
    par {clave : valor}
    -LA CLAVE DEBE SER UNICA- (dentro de un mismo diccionario)
    ->Si hay una clave repetida, devuelve el último valor asociado a la clave.
    
"""
#diccionario vacio
notas = {}
#crear diccionario con datos
notas = {
    "Camila" : 7, 
    "Antonio" : 7, 
    "Felipe" : 6,
    "Antonia" : 7,
    }

#Como acceder a los elementos||valores del diccionario.
print(notas["Camila"]) #7
print(notas["Antonio"]) #7
print(notas["Felipe"]) #6
print(notas["Antonia"]) #7
# print(notas["Pepe"]) #-> KeyError: 'Pepe' -> no lo encuentra o no existe o está mal escrito.
print("---------")

#Agregar par clave:valor al diccionario
#diccionario[clave]= valor
notas["Pepe"]= 5
print(notas) #{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'Antonia': 7, 'Pepe': 5}
print("---------")
notas["Juan"]= 7
print(notas) #{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'Antonia': 7, 'Pepe': 5, 'Juan': 7} -> siemrpe se agrega al final la nueva clave.
print("---------")

#Cambiar valor a una clave
notas["Felipe"]= 7 #cuando no crea, modifica automaticamente el valor
print(notas) # {'Camila': 7, 'Antonio': 7, 'Felipe': 7, 'Antonia': 7, 'Pepe': 5, 'Juan': 7}
print("---------")

##Eliminar elementos (2 formas)
#del
del notas["Antonia"]
print(notas) # {'Camila': 7, 'Antonio': 7, 'Felipe': 7, 'Pepe': 5, 'Juan': 7}
print("---------")

#pop -> ademas de borrar captura el elemento eliminado
eliminado = notas.pop("Antonio")
print(eliminado) # 7
print(notas) # {'Camila': 7, 'Felipe': 7, 'Pepe': 5, 'Juan': 7}
print("---------")

#Unir diccionarios
notas2 = {
    "Alexis" : 6,
    "Yasna" : 6,
    "Camila" : 3,
}
#Union con metodo update -> agrega la informacion del segundo diccionario al primero
notas.update(notas2)
#notas2.update(notas) -> "camila" : 7 reemplazara a "Camila" : 3
print(notas) # {'Camila': 3, 'Felipe': 7, 'Pepe': 5, 'Juan': 7, 'Alexis': 6, 'Yasna': 6} -> se queda con la ultima informacion de "Camila" : 3
#CUIDADO: Colision de igualdad de llaves.
print("---------")

