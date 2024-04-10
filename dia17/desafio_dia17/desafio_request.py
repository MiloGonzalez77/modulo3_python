import requests

#1. Obtenga toda la información de los usuarios retornada por la API, guárdela en una variable llamada users_data e imprímala en pantalla.
response_get = requests.get("https://reqres.in/api/users")
#Guardar en variable users_data
users_data = response_get.json()
#Impresion variable
print("Informacion de usuarios")
print(users_data)
print(response_get)
print("############")

#2. Cree un usuario que tenga de nombre Ignacio y de trabajo Profesor. Guarde el diccionario de respuesta en una variable llamada created_user e imprímala 
# en pantalla
payload_post = {
    "name": "Ignacio",
    "job": "Profesor"
}  
headers = {
'Content-Type': 'application/json'
}
#Metodo post para añadir el usuario
response_post = requests.post("https://reqres.in/api/users", headers=headers, json=payload_post)
#Guardar en variable created_user
created_user = response_post.json()
#Impresion de cambios
print(f'Nuevo Usuario ingresado: {created_user} - Codigo: {response_post}')
print("############")

#3. Actualice un usuario llamado morpheus para que tenga un campo llamado residence igual a zion. Guarde el diccionario de respuesta en una variable llamada 
# updated_user e imprímala en pantalla. 
payload_add = {
    "name": "morpheus"
}
headers = {
    'Content-Type': 'application/json'
}

response_add = requests.post("https://reqres.in/api/users", headers=headers, json=payload_add)
created_user = response_add.json()
#Impresion de cambios
print("Usuario añadido:")
print(created_user)
print("############")
#Actualizar en morpheus campo residence
payload_update = {
    "residence": "zion"
}

response_update = requests.put(f"https://reqres.in/api/users/{created_user['id']}", headers=headers, json=payload_update)
updated_user = response_update.json()
#Impresion de cambios
print("Usuario actualizado:")
print(updated_user)
print("############")

#4. Elimine un usuario llamado Tracey. Imprima el código de respuesta en pantalla. 
response = requests.delete("https://reqres.in/api/users/7")
#Impresion de cambios
print(f"Código de respuesta por usuario [Tracey] eliminado: {response.status_code}")
print("###### Fin de Programa ######")