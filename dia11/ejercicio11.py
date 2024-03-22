import os
from os import system 

###Comparar diccionarios
dic1 = {1:"uno",2:"dos"}
dic2 = {2:"dos",1:"uno"}
dic3 = {2:"dos",3:"tres"}
dic4 = {2:"dos",3:"cuatro"}
print(dic1==dic2) #True
print(dic1==dic3) #False
print(dic4==dic3) #False

#System(clear) para limpiar terminal
os.system("cls")

###DICCIONARIOS ANIDADOS

pares_impares = {
    "pares" : {
        2:"dos",
        4:"cuatro",
        6:"seis",
        8:"ocho",
        10:"diez"
        },
    "impar" : {
        "uno":1,
        "tres":3,
        "cinco":5,
        "siete":7,
        "nueve":9
        },
}

print("--------")
print(pares_impares) #{'pares': {2: 'dos', 4: 'cuatro', 6: 'seis', 8: 'ocho', 10: 'diez'}, 'impar': {'uno': 1, 'tres': 3, 'cinco': 5, 'siete': 7, 'nueve': 9}}
print("--------")

#Imprimir el valor "seis"
print(pares_impares["pares"]) #{2: 'dos', 4: 'cuatro', 6: 'seis', 8: 'ocho', 10: 'diez'}
print(pares_impares["pares"][6]) #seis

#Imprimir el valor 5
print(pares_impares["pares"])  #{2: 'dos', 4: 'cuatro', 6: 'seis', 8: 'ocho', 10: 'diez'}
print(pares_impares["impar"]["cinco"]) #5
#Se ingrese a cada diccionario anidado mediante corchetes.
print("-------")

#Metodo .key()
computador = {
    'notebook' : 489990,
    'tablet' : 120000,
    'cargador' : 12400,
}

print(computador.keys()) #dict_keys(['notebook', 'tablet', 'cargador'])
for key in computador.keys():
    print(key)
print("-------")
print(computador.values()) #dict_values([489990, 120000, 12400])
print("-------")
print(computador.items()) #dict_items([('notebook', 489990), ('tablet', 120000), ('cargador', 12400)])
for clave,valor in computador.items():
    print(f"")
print("-------")

