from sys import argv
#Filtrado Relevante.

#Diccionario de prueba
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

#definicion de arreglo para terminal
umbral = int(argv[1])

#Comparacion de umbral arg con diccionario
if len(argv) ==2:
    umbral2 = "mayor"
else:
    umbral2= argv[2].lower()
#Control de dato de datos:
def mayor (dato):
    if umbral2 == "mayor":
        productos = [producto for producto,valor in precios.items() if valor > dato ]
        print(f"los valores MAYORES al umbral son: {", ".join(productos)}")
    elif umbral2 =="menor":
        productos = [producto for producto,valor in precios.items() if valor < dato ]
        print(f"los valores MENORES al umbral son: {", ".join(productos)}")
    else: 
        print("la opción no es válida")

mayor(umbral)

#Arreglo para ejecutar:
#python dia13/desafio_dia13/filtro.py 30000