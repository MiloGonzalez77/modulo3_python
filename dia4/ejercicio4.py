"""
    Solicitar al usuario el ingreso de 3 numeros 
    y determinar cuales de ellos es mayor que 33.
    El usuario solo puede escribir numeros enteros del 1 al 100
    y determinar cual numero es mayor y cual es menor
"""

#Pasos
"""
    -Inicio
    
    Paso 1: Preguntar "Ingrese el primer numero (del 1 al 100)"
    -decision: es numero entero? 
    no: volver a preguntar paso 1
    si: avanzar a siguiente decision:
    -decision: es numero del 1 al 100?
    no: volver a preguntar paso 1
    si: registrar e imprimir dato.
    
    Paso 2: Preguntar "Ingrese el segundo numero (del 1 al 100)"
    -decision: es numero entero? 
    no: volver a preguntar paso 2
    si: avanzar a siguiente decision:
    -decision: es numero del 1 al 100?
    no: volver a preguntar paso 2
    si: registrar e imprimir dato.
    
    Paso 3: Preguntar "Ingrese el tercer numero (del 1 al 100)"
    -decision: es numero entero? 
    no: volver a preguntar paso 3
    si: avanzar a siguiente decisión:
    -decision: es numero del 1 al 100?
    no: volver a preguntar paso 3
    si: registrar e imprimir dato. 
    
    Paso 4: comparar numero 1 con 33
    -decision: numero 1 es mayor que 33?
    no: imprimir "el primer numero ingresado no es mayor que 33"
    si: imprimir "el primer numero ingresado es mayor que 33"
    
    Paso 5: comparar numero 2 con 33
    -decision: numero 2 es mayor que 33?
    no: imprimir "el segundo numero ingresado no es mayor que 33"
    si: imprimir "el segundo numero ingresado es mayor que 33"
    
    Paso 6: comparar numero 3 con 33
    -decision: numero 3 es mayor que 33?
    no: imprimir "el tercer numero ingresado no es mayor que 33"
    si: imprimir "el tercer numero ingresado es mayor que 33"
    
    Paso 7: comparar numeros 1, 2 y 3 (cual es mayor)
    -decision: numero 1 es mayor que 2?
    si: -decision: numero 1 es mayor que numero 3?
    no: -decision: numero 2 es mayor que numero 3?
        ->si: imprimir "el segundo numero ingresado es el numero mayor"
        ->no: imprimir "el tercer numero ingresado es el numero mayor"
    ->default: imprimir "el primer numero ingresado es el numero mayor"
    
    Paso 8: comparar numeros 1, 2 y 3 (cual es menor)
    -decisión: numero 1 es menor que 2?
    si: -decision: numero 1 es menor que numero 3?
    no: -decision: numero 2 es menor que numero 3?
        ->si: imprimir "el segundo numero ingresado es el numero menor"
        ->no: imprimir "el tercer numero ingresado es el numero menor"
    ->default: imprimir "el primer numero ingresado es el numero menor"
    
    -Fin.
"""

#Calcular el promedio con 2 decimales de 3 notas - ingresadas por el usuario:
"""
    -Pseudocodigo-
    Inicio
    leer nota 1
    leer nota 2
    leer nota 3
    Mostrar promedio con 2 decimales
    Fin
"""