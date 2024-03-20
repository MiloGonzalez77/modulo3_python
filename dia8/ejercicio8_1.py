#Transformando un ciclo for en un Comprehension

# solicitamos el número de pares a generar
n = 10
# generamos una lista vacía para almacenar los pares
lista_par = [] #-> Tamaño es 0.
for i in range(n):
# podemos hacer append de los valores generados
# en este caso partimos desde el 2
    lista_par.append(2*i + 2) #-> metodo lista.append() agrega valores al final de la lista
    print(f"Listando {lista_par}")
# mostramos el resultado
print(f"Lista de numeros pares: {lista_par}")

###Comprehension### -> es agregar de forma abreviada en una sola linea
#[formula for variable in iterable]
lista_par = [2*i + 2 for i in range(n)] #Resume 3 lineas de codigo en una sola.
print(lista_par)
print("--------")

#Condicionales con List Comprehensions
valores = [0,4,5,6,7,8,9]
divisibles = []
for valor in valores:
    if valor % 2 == 0:
        divisibles.append('Divisible')
    else:
        divisibles.append('No Divisible')
print(f"Lista divisibles: {divisibles}")
print("#######")
#[expresión1 if condición1 else expresión2 for variable in iterable]
divisibles2 = ['Divisible' if valor % 2 == 0 else 'No Divisible' for valor in valores ]
print(divisibles2)
print("#######")

#Operaciones de filtrado
lista = ['Lechugas', 'Tomates', 5, 10, True, False, True, 'Papas', 5.1, 45.2, 1, 2, 0]
count_str = 0
count_int = 0
count_flo = 0
lista_str= []
lista_int = []
lista_flo = []

for elemento in lista:
    if type(elemento) is str:
        count_str += 1
        lista_str.append(elemento)
    if type(elemento) is int:
        count_int += 1
        lista_int.append(elemento)
    if type(elemento) is float:
        count_flo += 1
        lista_flo.append(elemento)
print(f"Hay [{count_str}] strings.")
print(f" Lista String: {len(lista_str)} - {lista_str}")
print(f"Hay [{count_int}] int.")
print(f" Lista Int: {len(lista_int)} - {lista_int}")
print(f"Hay [{count_flo}] float.")
print(f" Lista Float: {len(lista_flo)} - {lista_flo}")
print("#######")
