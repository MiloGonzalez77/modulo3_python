#Actividad 2 - Primeros auxilios

#Se requiere la construcción de una aplicación interactiva
# que entregue los distintos pasos a seguir dependiendo de las respuestas 
# que el usuario entrega en tiempo real. 

opciones = ['si', 'no']


#Inicio
print("###### Primeros Auxilios ######")
print(f"Programa iniciado: Recuerde responder a las preguntas escribiendo: {opciones}")

#Responde estimulos?
opcion = input("¿Responde a estimulos?\n")
if opcion != 'si' and opcion != 'no':
    print(f"Respuesta invalida. Las respuestas validas son: {opciones} - reinicia programa")
elif opcion == 'si':
        print("Valorar la necesidad de llevarlo al hospital mas cercano.")
else:
    print("Abrir via respiratoria.")
    #Respira?
    opcion = input("¿La persona respira?\n").lower()
    if opcion == 'si':
        print("Permitale adquirir posicion de ventilacion.")
    elif opcion == 'no':
        print("Administre 5 ventilaciones y llame ambulancia.")
            
        #signos de vida? // 
        while opcion in opcion: 
            input("¿Tiene signos vitales?\n").lower()
            if opcion == 'no':
                print("Administre compresiones torácicas hasta que llegue la ambulancia.")
            elif opcion == 'si':
                print("Reevaluar a la espera de ambulancia")
            else:
                print(f"Respuesta invalida. Las respuestas validas son: {opciones} ")
            
            #llego ambulancia?
            ambulancia = input("¿Llegó la ambulancia?\n").lower()
            if ambulancia == 'no':
                print("Reevalue mientras espera ambulancia")
            elif ambulancia == 'si':
                break
            else:
                print(f"Respuesta invalida. Las respuestas validas son: {opciones} ")
    else:
        print(f"Respuesta invalida. Las respuestas validas son: {opciones} - reinicia programa")
print("###### Fin de programa ######")
