#Alertas Telematicas

#Lista velocidades
velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
            14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
            14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
            14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
            10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
            11, 10, 18, 10, 14, 5, 23, 20, 23, 21
]
#funcion para retornar el promedio de las velocidades
def cacular_promedio (lista):   
    #se devuelve la suma de la lista divido por el largo del arreglo 
    return sum(lista)/len(lista)

#se crea una función que usa el promedio y se crea arreglo con los valores mayores al promedio
def lista_posiciones(lista):
    promedio = cacular_promedio(velocidad)
    print(promedio)
    posiciones = [valor for valor in range(len(lista)) if lista[valor]>promedio]
    return posiciones
#impresion en pantalla
print(f"Lista posicion velocidades mayores al promedio: {lista_posiciones(velocidad)}")