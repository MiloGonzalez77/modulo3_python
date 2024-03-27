#Mni Encuesta

#Funcion menu de respuestas
def imprimir_menu():
    print("Opciones: ")
    print("1. De acuerdo")
    print("2. En desacuerdo")
    print("3. No me interesa")

#Lista de Preguntas
preguntas = ['Enunciado Pregunta 1','Enunciado Pregunta 2','Enunciado Pregunta 3']
respuestas = []

#Despliegue de encuesta
"""
print(preguntas[0])
imprimir_menu()
respuestas.append(input("> \n"))

print(preguntas[1])
imprimir_menu()
respuestas.append(input("> \n"))

print(preguntas[2])
imprimir_menu()
respuestas.append(input("> \n"))
""" 
for pregunta in preguntas:
    print(pregunta)
    print(" ")
    imprimir_menu()
    respuestas.append(input("> \n"))
    print(" ")

#Resumen de respuestas:
print(f"Respuestas: ")
"""
print(f"Respuesta 1: {respuestas[0]}")
print(f"Respuesta 2: {respuestas[1]}")
print(f"Respuesta 3: {respuestas[2]}")
"""
for i in range(len(respuestas)): #3 -> [0-2]
    print(f"La respuesta a la pregunta {i+1} es: {respuestas[i]}")
print(" ")
print("Fin de Programa.")
