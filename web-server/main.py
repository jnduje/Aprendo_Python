import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse # para responder n HTML

app = FastAPI() # creo una instancia de la aplicación fastAPI

@app.get('/')       # decorador
def get_list():     # creo el recurso
    return [1,2,3,]

'''
@app.get('/contact')
def get_list():
    return {"name": "Platzi"}
'''
# Así responde FastAPI en HTML
@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>
    """
    
def run():
    store.get_categories()

if __name__ == '__main__':
    run()