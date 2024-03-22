#CONVERSIONES

from sys import argv

"""
    Crear estructura de datos apropiada que permita ingresar tasas de conversión. 
    Las distintas tasas de conversión se deben ingresar mediante sys.argv en el siguiente orden: Sol, Peso Argentino, Dólar Americano. 
    
    Peso Chileno:
    a Sol peruano: 0.0046
    a Peso Argentino: 0.093
    a Dólar Americano: 0.00013
    -python conversiones.py 0.0046 0.093 0.0013 10000
    
    Respuesta esperada:
    Los 10000 pesos equivalen a:
    46.0 Soles
    930.0 Pesos Argentinos
    13.0 Dólares

"""

#Arreglo de entrada: dia12/desafio4/conversiones.py 0.0046 0.093 0.0013 10000
print(" ------ INICIO ------ ")
#monedas

sol_peruano = float(argv[1])
peso_argentino =float(argv[2])
dolar_americano =float(argv[3])
peso_chileno = float(argv[4])

#conversiones 

print("")

print(f"Los {round(peso_chileno)} pesos chilenos equivalen a: ")
print(f"{sol_peruano*peso_chileno} Soles ")
print(f"{peso_argentino*peso_chileno} Pesos Argentinos ")
print(f"{dolar_americano*peso_chileno} Dólares ")

print("")
print(" ------ FIN ------ ")