#Actividad 1 - Filtrado compacto
import sys

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

#Se solicita devolver un informe resumido que exponga los meses que superan un cierto umbral.
#Ejemplo: python dia9/mayor_a.py 40000

informe = int(sys.argv[1])
informe_umbral = {}
#Comparacion e impresion de meses y valores que superan el umbral
for clave, valor in ventas.items():
    if valor > informe:
        informe_umbral[clave] = valor 
        #print(f"Informe: {clave} - {valor}")
print(f"Diccionario Informe: {informe_umbral}")
        
print("---Fin de Programa---")