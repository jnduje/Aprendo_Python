from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI         #FastAPI trabaja sobre Pydantic
from fastapi import Body, Query, Path

app = FastAPI()

#Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None



#Path operation decorator. Utiliza el métogo get que viene de la instancia app.
@app.get('/')
def home():         #Path function
    return {'Hello': 'World'}

#Request and Response Body
@app.post('/person/new') # post es un método que se utiliza cuando el cliente envía a la pág web
def create_person(person: Person = Body (...)): # EL "..." significa que ese parámetro es obligatorio
    return person

#Validations: Query Parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,   #valido que el nombre tenga entre 1 y 50 caracteres
        max_length=50,
        title= 'Person Name',
        description= 'This is the person name between 1 and 50 characters'
        ), 
    age: Optional[str] = Query(
        ...,
        title='Person Age',
        description="This is the person age. It's requiered"
        )
):
    return {name: age}


# Validations: Path Parameters
@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title=" Person ID",
        description="It's the description of Person ID")
):
    return {person_id: 'It exists!'}