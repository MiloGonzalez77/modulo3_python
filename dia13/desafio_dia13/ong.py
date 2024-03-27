#Apoyo matematico

#Calcular el factorial de un numero:
def factorial(numero):#5! = 5*4*3*2*1
    valor = 1 # variable acumuladora
    for n in range(1,numero+1):#1,2,3,4,5
        valor = valor * n
    return valor
#Ejemplo:
#print("el factorial es:",factorial(6))

#Calculo de la productoria
def productoria(lista):
    valor = 1
    for elemento in lista:
        valor *= elemento
    return valor
#Ejemplo:
#print(productoria([4, 6, 7, 4, 3]))

#Función que permita controlar los cálculos:
def calcular(**parametros): #* tupla; ** diccionario 
    for clave,valor in parametros.items():
        if "fact" in clave:
            print(f"El factorial de {valor} es {factorial(valor)}")
        else:
            print(f"La productoria de {valor} es {productoria(valor)}")

#Llamado al metodo
calcular(fact_1 = 5, prod_1 = [4, 6, 7, 4, 3], fact_2 = 6)
