#Separación decima (etc) de float es "."
#Division entre integers, el resultado es float.

print(4/2) #2.0
print(5/2) #2.5
print(5/3.5)
print(2.4*4)
#Se pueden combinar operaciones aritmesticas entre int y float

nombre="Milo"
apellido="gonzalez"
año=2024
print(3*nombre)
print(año*2)
# print(nombre/2) -> Terminal indica que no se puede dividir string.

#Metodo count() -> busca y cuenta las veces que existe un caracter en un string
print("Saitama".count("a"))
print(nombre.count("i"))

#Metodos upper() y lower()
print("Saitama".upper()) #SAITAMA -> todo en mayuscula
print("SaItAmA".lower()) #saitama -> todo en minucula
print(nombre.upper())
print(nombre.lower())

#Metodo title()
print("333sAiTaMa".title()) #Saitama  -> solo primera letra en mayuscula

#len()
print(len(" camilo gonzalez ")) #17 -> cuenta todos los caracteres dentro del "", incluidos los espacios

#join()
print(", ".join(["a","b","c"])) #a, b, c -> une strings separados ingresados al arreglo con un string de arreglo para separarlos, similar a una concatenacion
print("-".join(["Camilo","Gonzalez","Ulloa"]))

#Salto de linea \n
print("escribir\ncon salto\nde linea")
"""
escribir
con salto
de linea
"""

#Tipos de datos
canitdad_alumnos=30
peso=85.5
verdadero=True
print(type(nombre)) #<class 'str'>
print(type(año)) #<class 'int'>
print(type(peso)) #<class 'float'>
print(type(verdadero)) #<class 'bool'>

type(verdadero) #No imprime datos, ya que no tiene funcion Pint()

#Manipulacion de datos
numero = 2
numero = numero + 3 # -> 2+3 - se reasigna variable
print(numero) #5

nombre = nombre + " Gonzalez Ulloa" 
print(nombre) # Milo Gonzalez Ulloa

print(5/9) #0.5555555555555556
#precision de datos con interpolacion
print(f"resultado division {5/9:.2f}") # 0.56 
print("resultado de division",round(5/9,3)) # 0.556 -> Metodo round, se ocupa mas.

#INPUT - ingreso de datos
nombre = input("Ingrese su nombre: ")
print(f"Hola, tu nombre es {nombre.title()}")
edad = input("Ingresa tu edad: ")
print(f"Tienes {edad} años.")
print(type(edad)) #arroja como dato <class 'str'>
