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

#Metodo .get()
print(notas.get("Camila")) #3
#.get() con control de error
print(notas.get("Lucho","Valor no encontrado")) #Valor no encontrado -por default.
print(notas2.get("Goku")) #None

prueba = notas.get("Julio")
print(prueba) #None
print(type(prueba)) #<class 'NoneType'>
print("-------")

#agregar con metodo set default
notas.setdefault("Lucas",10)
print(notas) #{'Camila': 3, 'Felipe': 7, 'Pepe': 5, 'Juan': 7, 'Alexis': 6, 'Yasna': 6, 'Lucas': 10}
notas.setdefault("Lucas",2)
#si la clave existe retorna el valor actual y no lo reemplaza
print(notas) #{'Camila': 3, 'Felipe': 7, 'Pepe': 5, 'Juan': 7, 'Alexis': 6, 'Yasna': 6, 'Lucas': 10}
print("-------")
notas.setdefault("Valeria")
print(notas) # {'Camila': 3, 'Felipe': 7, 'Pepe': 5, 'Juan': 7, 'Alexis': 6, 'Yasna': 6, 'Lucas': 10, 'Valeria': None}
notas["Valeria"]=6
print(notas) # {'Camila': 3, 'Felipe': 7, 'Pepe': 5, 'Juan': 7, 'Alexis': 6, 'Yasna': 6, 'Lucas': 10, 'Valeria': 6}
print("-------")

### ELIMINAR Y RASPALÑDAR EN OTRO DICCIONARIO.
eliminados = {}
# eliminados = eliminados.setdefault(notas.pop("Pepe")) --->no resulta
eliminados["Pepe"]=notas.pop("Pepe") #---> eliminamos pepe desde notas y guardamos en diccionario eliminados.
print(notas) #{'Camila': 3, 'Felipe': 7, 'Juan': 7, 'Alexis': 6, 'Yasna': 6, 'Lucas': 10, 'Valeria': 6}
print(eliminados) #{'Pepe': 5}
print("--------")

tupla1 = notas.popitem() #elimina el ultimo elemento del diccionario y devuelve la tupla (clave:valor) -la tupla es similar a la lista pero inmutable //no se puede modificar
#print(notas.popitem()) #('Lucas', 10)
print(notas) #{'Camila': 3, 'Felipe': 7, 'Juan': 7, 'Alexis': 6, 'Yasna': 6}
print(" ")
print(tupla1[0]) # Valeria
print(tupla1[1]) # 6
#tupla1[1]="mishi"
#print(tupla1[1]) - TypeError: 'tuple' object does not support item assignment
print("--------")

notas.clear() #elimina los elementos dejando diccioanrio vacio
print(notas) #{}
print("--------")
