import requests

#metodo para obtener datos de la API
def obtener_datos():
    url = 'https://aves.ninjas.cl/api/birds'
    response = requests.get(url)
    return response.json()