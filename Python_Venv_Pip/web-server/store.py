import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code) #Estado en HTTP
    print(r.text)   # Información de la API (devuelve un string)
    print(type(r.text))

    categories = r.json()   # En vez de preguntar por text pregunto por formato json.
                            # Formato de lista de diccionarios que Python puede interpretar
    
    for category in categories:
        print(category['name'])

    