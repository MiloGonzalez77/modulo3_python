#Transformando segundos a minutos
"""
    Se tiene una lista con la cantidad de segundos que demoraron algunos procesos.
    Se necesita una función para transformar todos los datos a minutos, (se requiere 
    sólo la parte entera, la parte decimal se puede ignorar).
    seconds = [100, 50, 1000, 5000, 1000, 500]

"""
segundos = [100, 50, 1000, 5000, 1000, 500]

minutos = [segundo// 60 for segundo in segundos]
print(f"Lista minutos: {minutos}")
