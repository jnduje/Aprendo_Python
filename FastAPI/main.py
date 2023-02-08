from fastapi import FastAPI

app = FastAPI()

#Path operation decorator. Utiliza el métogo get que viene de la instancia app.
@app.get('/')
def home():
    return {'Hello': 'World'}
