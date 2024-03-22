from sys import argv
# argumento = argv[1]

with open(f"dia12/desafio4/lorem_ipsum.txt", "r") as file:
    texto=file.read()
    
print(" -------- INICIO PROGRAMA ------- \n")

#contador de letras 
""" 
    
letras =[]
for i in texto:
    letras.append(i)
    
"""
# ----- OPTIMIZACIÓN DEL CICLO Y LISTA ------
letras =[i for i in texto]
letras_convertidas =set(letras)
# print (type(letras_convertidas))
print (f"El número de caracteres distintos es: {len(letras_convertidas)}")    

#contador de palabras
palabras = texto.split(" ")
# print(palabras)
palabras_convertidas =set(palabras)
# print (type(palabras_convertidas))
print (f"El número de palabras distintas es: {len(palabras_convertidas)}\n")    

print(" ------- FIN PROGRAMA ------- ")